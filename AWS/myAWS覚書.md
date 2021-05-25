# myAWS 覚書

## アカウント

google keep

## EC2 インスタンス

- t2.micro とかいう無料枠を立ち上げ中
- インスタンス名 : google keep
- root の成り方 : sudo su -
- EC2-ElasticIP で IP 永続化中 : EC2 見ろ
- route53 で DNS 設定中
- route53 で サブドメインその 1 設定中 - recordset : route53 見ろ。login.のやつ
- EC2-セキュリティグループのインバウンドで 8080
- route53 で サブドメインその 1 設定中 - recordset : route53 見ろ。login.のやつ

### nginx 設定

- インスコ : 入れる
- 場所 : /etc/nginx
- やること 1 : conf.d -> server.conf をいじる
- 設定ファイル変更 : sudo vi (ファイル名)
- location 設定 :
  ```conf
  location / {
      root /usr/share/nginx/html/ikebxxxxx;
      index index.html index.php index.htm
  }
  ```
- 保存 : :wq
- curl で確認 : curl -H "Host:www.ikeb.w" http://localhost/index.html

### サイトドメインとの関連付け（Route53）

- A レコードを追加。 : WWW.ikb.w
- http://www.ikb.w

## RDS 用意

- パラメータグループ設定 : 日本語 OK なように Charset を変更
- オプショングループ設定 : mySQL って書いただけ
- DB インスタンス識別子 : omy-dev1-instance01
- マスターユーザー名 : db_master_user
- マスターパスワード : db_master_password
- インスタンス名 : start_aws_wordpress_dbname
- エンドポイント : omy-dev1-instance01.cnecvoe57swz.ap-northeast-1.rds.amazonaws.com
- セキュリティグループ設定 : rds-launch-wizard から インバウンドルール TCP3306 を設定。ソースに「マイ IP」を指定したけど、これはどうなんだろう。将来めんどくさそう。

### EC2 から入って適当にテーブルとか準備

- EC2 に入る
- mysql -h (endpoint) -u (masteruser) -p
- password 入れる
- DB を作る
- table を作る

### RDS と A5M2 の連携

- ホスト名 : エンドポイント
- ポート : 3306
- ユーザー : 上の通り
- パスワード : 上の通り

## KMS 用意

## Secrets Manager

- シークレットの種類 : RDS データベースの認証情報
- このシークレットのユーザー名 : rds01
- 〃 パスワード : RDS01
- 暗号化キー : DefaultEncryptionKey（なんか最初から存在しているやつを選んだ。なんだろうね）

- シークレットの名前 : mySecret01

- 自動ローテーション : 無効

```Python
# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developers/getting-started/python/

import boto3
import base64
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "mySecret01"
    region_name = "ap-northeast-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    # Your code goes here.

```

### EC2 から接続 Secrets Manager 情報で接続

- aws cli を利用するらしい
- まずは EC2 に Python3 をインストール :
  - いつのまにかなんか入ってた？ わからん。1 年前か（sudo yum install phthon3 -y）
- pip を単独でインストール。Python2 用。Python3 は pip3 ってのらしいけどもうめんどいから。 : yum -y install python-pip
- AWS CLI インストール : sudo pip install awscli --upgrade --user
- シークレット情報確認 : aws secretsmanager describe-secret --secret-id mySecret01

## なんか

# AWS KMS、Parameter Store、Secrets Manager の対比表

そもそもそれぞれなにか。

## AWS Key Management Service (KMS)

データの暗号化やデジタル署名に使用するキーを簡単に作成して管理する、暗号鍵管理サービス。名称の通り。

## AWS Systems Manager パラメータストア

AWS の機能を活用したアプリコードと ID/パスワード情報の分離の有力な方法。  
2018 年初頭まで。

## AWS Secrets Manager

ID/パスワードや認証情報の管理サービスとして、2018 年 4 月に登場。

ローテーションは有効/無効が選択できる。
ローテーションが影響するのは外部ツール。プログラムには影響しない。
Secrets Manager には ID/Pass モードも存在し、もうこれでええじゃろ。

## まとめ

Secrets Manager おすすめ。コンソール使いやすいし
