# -*- coding: utf-8 -*-
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# input pattern
# normal - 1
s = input().strip()
# normal - 2
n = int(input())
# Split : aaa 111
s = input().strip().split(" ")
print(str(s[0]))
print(int(s[1]))
# 配列に格納 : 1行づつ無限input : break必須
l = []
while True:
    try:
        l.append(int(input().strip()))
    except EOFError:
        break
# 配列に格納:固定ループ
s = []
for i in range(3):
    s.append(input())
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D048 台風の間隔
l = []
while True:
    try:
        l.append(int(input().strip()))
    except EOFError:
        break

# for i in range(1, len(l)):
#    print(l[i] - l[i-1])
for i, o in enumerate(l):
    if i == 0:
        continue
    print(l[i] - l[i-1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D007:N倍の文字列
n = int(input())
s = "*" * n
print(s)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D050:お月見だんご
s = input().strip().split(" ")
n1 = int(s[0])
n2 = int(s[1])

if n1 > 5:
    n1 = 5

if n2 > 5:
    n2 = 5

print(n1 + n2)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D050:お月見だんご
s = input().strip().split(" ")
n = 0
# indexいらん場合はこちら↓
for o in s:
    # for i, o in enumerate(s):
    if o == 'W':
        n += 1
        if n == 5:
            break

x = "OK" if n == 5 else "NG"
print(x)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D052:ピラミッドの作り方
# coding: utf-8
n = int(input())
a = (n * (n + 1)) / 2
print(int(a))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D053:トリック・オア・トリート
# coding: utf-8
s = input().strip()
ans = "Thanks!" if s == "chocolate" or s == "candy" else "No!"
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D054:11/11
# coding: utf-8
n = len(str(input().strip()))
ans = "OK" if n >= 11 else 11 - n
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D055:ワインのキャッチコピー
# coding: utf-8
s = input()
print("Best in " + s)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D056:かまくらづくり
# coding: utf-8
s = input().strip().split(" ")
n1 = int(s[0])
n2 = int(s[1])

print(n1 ** 3 - n2 ** 3)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D057:プレゼント選び
# coding: utf-8
n = int(input())
s = input().strip().split(" ")
print(s[n-1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D058:初詣で
# coding: utf-8
s = input().strip().split(" ")
n1 = int(s[0])
n2 = int(s[1])
n3 = int(s[2])
print("A" * n1 + "B" * n2 + "A" * n3)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D059:トランプ占い
# coding: utf-8
s = input().strip().split(" ")
if s[0] == "J" and s[0] == s[1]:
    s[1] = "Q"
print("{0} {1}".format(s[0], s[1]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D060:AボタンとBボタン
# coding: utf-8
s = input().strip().split(" ")
n1 = int(s[0])
n2 = int(s[1])
print(n1-n2)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D061:3倍返し？
# coding: utf-8
n = int(input())
ans = 1 if n == 0 else n * 3
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D062:ひな祭り
# coding: utf-8
s = input().strip().split(" ")
n1 = int(s[0])
n2 = int(s[1])
n3 = int(s[2])

ITEMS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def f(a1, a2):
    ans = ""
    for i in range(a1, a2):
        ans = ans + ITEMS[i]
    return ans


print(f(0, n1))
print(f(n1, n1+n2))
print(f(n1+n2, n1+n2+n3))

# その2↓
# coding: utf-8
s = input().strip().split(" ")
s = list(map(int, s))  # 数値変換
hina = "ABCDEFGHIJ"
print(hina[:s[0]])
print(hina[s[0]:(s[0] + s[1])])
print(hina[(s[0] + s[1]):])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D063:お花見の場所取り
# coding: utf-8
ns = input().strip().split(" ")
me = int(input())
ans = 0
for i in range(5):
    if (int(ns[i]) < me):
        ans += 1
    else:
        break
ans += 1
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D064:嘘つきの日
# coding: utf-8
s = input().strip()
ans = s.replace('False', 'True')
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D065:エラーコードの分類
# coding: utf-8
s = int(input())
n = int(s / 100)
ans = "unknown"
if n == 2:
    ans = "ok"
elif n == 4:
    ans = "error"
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D066:スタミナの計算
s = input().strip().split(" ")
n1 = int(s[0])
n2 = int(s[1])

ans = "No" if n2-n1 < 0 else n2-n1
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D067:スイッチのオンオフ
# coding: utf-8
n = int(input())
ans = "OFF"
if n % 2 != 0:
    ans = "ON"
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D068:雨と晴れの記録
# coding: utf-8
n = int(input())
s = input().strip()
a1 = 0
a2 = 0
for i in range(n):
    if s[i] == "S":
        a1 += 1
    else:
        a2 += 1
print("{0} {1}".format(a1, a2))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D069:割り切れない平均点
# coding: utf-8
s = input().strip().split(" ")
s = list(map(int, s))  # 数値変換
print(round(sum(s) / len(s), 1))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D070:残りのページ
# coding: utf-8
s = input().strip().split(" ")
n = list(map(int, s))  # 数値変換
print(n[0] - n[1])

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D071:洗濯物と砂ぼこり
# coding: utf-8
s = input().strip().split(" ")
n1 = int(s[0])
n2 = int(s[1])
ans = "No"
if n1 >= 25 and n2 <= 40:
    pass
elif n1 >= 25 or n2 <= 40:
    ans = "Yes"
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D072:データのバックアップ
# coding: utf-8
import math
s = input().strip().split(" ")
n = list(map(int, s))  # 数値変換
print(math.ceil(n[0] / n[1]) * n[2])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# D073:文字の反転
# coding: utf-8
s = input().strip()
print(s[::-1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ロジックサマナー : オートチャージ　(封印レベルC)
# coding: utf-8
s = input().strip().split(" ")
n1 = list(map(int, s))  # 数値変換

s = input().strip().split(" ")
n2 = list(map(int, s))  # 数値変換

for i in range(n1[0]):
    n1[1] += n2[i]

    if n1[1] <= n1[2]:
        n1[1] += n1[3]

print(n1[1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C005:アドレス調査
# coding: utf-8
cnt = int(input())
for i in range(cnt):
    s = input().strip().split(".")
    if len(s) != 4:
        print("False")
        continue

    ans = "True"
    for j in range(len(s)):
        if s[j].isdigit():
            n = int(s[j])
            if n in range(0, 256):
                continue
            else:
                ans = "False"
        else:
            ans = "False"
    print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C006:ハイスコアランキング
# coding: utf-8
s = input().strip().split(" ")  # アイテム数N、プレイ人数M、ランキング順位K
n1 = list(map(int, s))  # 数値変換

s = input().strip().split(" ")  # 得点Ci
n2 = list(map(float, s))  # 数値変換

score = [0 for i in range(n1[1])]  # 人数分の成績

for i in range(n1[1]):  # 一人ずつ設定
    s = input().strip().split(" ")  # 所持数Xi
    n3 = list(map(int, s))  # 数値変換

    for j in range(n1[0]):
        score[i] += n2[j] * n3[j]

score.sort()
score.reverse()

for i in range(n1[2]):
    print(int(score[i] + 0.5))  # python3 の round のアレにハマる。
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C008:文字列の抽出
# coding: utf-8
s = input().strip().split(" ")  # tagA 0 : tagB 1
line = str(input().strip())  # str

lenA = len(s[0])
lenB = len(s[1])

n1 = n2 = 0

while True:
    n1 = line.find(s[0], n1)
    n2 = line.find(s[1], n1+lenA)

    if n1 < 0 or n2 < 0:
        break

    if n1 + lenA == n2:
        print("<blank>")
    else:
        print(line[n1 + lenA: n2])

    # posずらし
    n1 = n2 + lenB
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C010:安息の地を求めて
# coding: utf-8
s = input().strip().split(" ")
n1 = list(map(int, s))  # int変換

cnt = int(input())

for i in range(cnt):
    s = input().strip().split(" ")
    n3 = list(map(int, s))  # int変換

    if ((n3[0] - n1[0]) ** 2) + ((n3[1] - n1[1]) ** 2) >= (n1[2] ** 2):
        print("silent")
    else:
        print("noisy")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C013:嫌いな数字
# coding: utf-8
n1 = input().strip()
cnt = int(input())

lst = []
for i in range(cnt):
    n2 = input().strip()
    if n1 not in n2:
        lst.append(n2)

if len(lst) == 0:
    print("none")
else:
    for item in lst:
        print(item)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C014:ボールが入る箱
# coding: utf-8
s = input().strip().split(" ")
n1 = list(map(int, s))   # int変換

for i in range(n1[0]):
    s = input().strip().split(" ")
    n2 = list(map(int, s))   # int変換

    if min(n2) >= n1[1] * 2:
        print(i + 1)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C015:ポイントカードの計算
# coding: utf-8
import math

cnt = int(input())

sum = 0
for i in range(cnt):
    s = input().strip().split(" ")
    a = str(s[0])
    n = int(s[1])

    if "3" in a:
        sum += math.floor(n / 100 * 3)
    elif "5" in a:
        sum += math.floor(n / 100 * 5)
    else:
        sum += math.floor(n / 100)

print(sum)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C016:Leet文字列
# coding: utf-8
import string
s = input().strip()
print(s.translate(str.maketrans('AEGIOSZ', '4361052')))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C017:ハイアンドロー・カードゲーム
# coding: utf-8
s = input().strip().split(" ")
p = list(map(int, s))  # int変換

for i in range(int(input())):
    s = input().strip().split(" ")
    c = list(map(int, s))  # int変換

    ans = "Low"
    if c[0] < p[0]
    ans = "High"
    elif c[0] == p[0] and p[1] < c[1]
    ans = "High"

    print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C018:何人前作れる？ 境界値だけNG
# coding: utf-8
#############


def getl(n):
    l = []
    for i in range(n):
        s = input().strip().split(" ")
        s[1] = int(s[1])
        l.append(s)
    return l


##############
l1 = getl(int(input()))
l2 = getl(int(input()))

ans = 100000
for o1 in l1:
    for o2 in l2:
        if o1[0] in o2:
            if o2[1] // o1[1] < ans:
                ans = o2[1] // o1[1]
            break

if ans == 100000:
    ans = 0

print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C019:完全数とほぼ完全数
# coding: utf-8
cnt = int(input())
for i in range(cnt):
    n = int(input())

    for i in range(n):
        if n % i == 0:
            sum += i

    ans = "neither"
    if n == sum:
        ans = "perfect"
    elif abs(n - sum) == 1:
        ans = "nearly"

    print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C020:残り物の量
# coding: utf-8
s = input().strip().split(" ")
n = list(map(int, s))  # int変換
a1 = n[0] - (n[0] * (n[1] / 100))
a2 = a1 - (a1 * (n[2] / 100))

print(a2)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C021:暴風域にいますか？
# coding: utf-8
s = input().strip().split(" ")
n = list(map(int, s))  # int変換

d1 = n[2] ** 2
d2 = n[3] ** 2

for i in range(int(input())):
    s = input().strip().split(" ")
    p = list(map(int, s))  # int変換

    x = (p[0] - n[0]) ** 2
    y = (p[1] - n[1]) ** 2
    xy = x + y

    ans = "yes" if d1 <= xy <= d2 else "no"

    print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# コードサマナーの惚れ薬Bだっけ？
# coding: utf-8
cnt = int(input())
l = []
ngpos = []
goukei = 0

hanten = False  # false = 横を計算 : true = 縦で計算

# いったん全部読み込みつつ、合計値を出しとく
for i in range(cnt):
    s = input().strip().split(" ")
    aaa = list(map(int, s))  # int変換

    if goukei < sum(aaa):
        goukei = sum(aaa)

    if aaa.count(0) > 0:
        # 1
        ngpos.append([i, aaa.index(0)])
        # 2
        if aaa.count(0) == 2:
            ngpos.append([i, len(aaa) - aaa[::-1].index(0) - 1])
            hanten = True

    l.append(aaa)

if hanten:
    l = list(map(list, zip(*l)))
    ngpos[0][0], ngpos[0][1] = ngpos[0][1], ngpos[0][0]
    ngpos[1][0], ngpos[1][1] = ngpos[1][1], ngpos[1][0]

# calc
for i in range(2):
    l[ngpos[i][0]][ngpos[i][1]] = goukei - sum(l[ngpos[i][0]])

if hanten:
    l = list(map(list, zip(*l)))

for i in range(cnt):
    print(" ".join([str(x) for x in l[i]]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# B012:チェックディジット
# coding: utf-8
for i in range(int(input())):
    esum = 0
    osum = 0

    s = input().strip()
    s = s.replace("X", "0")

    for i, c in enumerate(s):
        n = int(c)
        if i % 2 == 0:
            temp = n * 2
            if temp >= 10:
                a = str(temp)
                temp = int(a[0]) + int(a[1])
            esum += temp
        else:
            osum += n

    ans = 10 - ((esum + osum) % 10)
    if ans == 10:
        ans = 0

    print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# B004:ログファイルの抽出
# coding: utf-8
#############


def isValidIp(m, c):
    ret = False
    if m == "*" or m == c:
        ret = True
    elif m[0] == "[":
        a = m.split("-")
        ss = int(a[0].replace("[", ""))
        ee = int(a[1].replace("]", ""))
        if ss <= int(c) <= ee:
            ret = True
    return ret


#############
mip = input().strip().split(".")
for i in range(int(input())):
    s = input().strip().split(" ")
    # ip 判定
    tip = s[0].split(".")
    print(tip)
    if mip[0] == tip[0]
    and mip[1] == tip[1]
    and isValidIp(mip[2], tip[2])
    and isValidIp(mip[3], tip[3]):
        print(s[0] + " " + s[3][1:] + " " + s[6])

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# C022:ローソク足
# coding: utf-8
l = [0, 0, 0, 1000000]
cnt = int(input())
for i in range(cnt):
    s = input().strip().split(" ")
    n = list(map(int, s))  # int変換

    if i == 0:  # start
        l[0] = n[0]

    if i == cnt - 1:  # end
        l[1] = n[1]

    if l[2] < n[2]:  # high
        l[2] = n[2]

    if l[3] > n[3]:  # low
        l[3] = n[3]

print(" ".join([str(x) for x in l]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D101 偶数派と奇数派
s = input().rstrip().split(' ')

a = int(s[0]) % 2
b = int(s[1]) % 2

if a + b == 1:
    print("YES")
else:
    print("NO")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D086 門松の作成
# s = input()

x = int(s) / 3

a = x * 3
b = x * 5
c = x * 7

print(int(a+b+c))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D084 英語で何月？
s = input()
d = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
     6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
     11: "November", 12: "December"}

val = d[int(s)]
print(val)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D109 ゾロ目の日付
s = input().rstrip().split(' ')
ss = s[0] + s[1]

a = s[0][0]

b = True

for x in ss:
    if x != a:
        b = False

if b:
    print("Yes")
else:
    print("No")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D109 ゾロ目の日付 その２
s = input().rstrip().split(' ')
ss = s[0] + s[1]

if len(ss) == ss.count(s[0][0]):
    print("Yes")
else:
    print("No")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D076: 禁止ワード
s = input()
s2 = input()

if s in s2:
    print("NG")
else:
    print(s2)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# リハビリ
s = "aiueoaiu"

i = s.count("ai")

if i:
    print("not 0 : count ->" + str(i))
else:
    print("zero desu")

s2 = s.replace("ai", "x")

print(s2)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D082:2つの単語
s = input()
s2 = input()

if s[-1] == s2[0] and s2[-1] != 'n':
    print("OK")
else:
    print("NG")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D092:花見の準備
s = input().rstrip().split(' ')
ss = input().rstrip().split(' ')

i = [int(n) for n in s]
ii = [int(n) for n in ss]
ans = i

p = int(i[2] / (i[0] * i[1]))
p2 = int(ii[2] / (ii[0] * ii[1]))

if p == p2:
    print("DRAW")
else:
    if p > p2:
        ans = ii

    print(" ".join([str(x) for x in ans]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D079:同じ文字
s = input()
print("NG" if len(s) == s.count(s[0]) else "OK")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D096:含んではいけない文字
s = input()

if 'I' in s or 'i' in s or 'l' in s:
    print("caution")
else:
    print(s)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D093:切りの良い番号
s = input()

print(s if len(s) == s.count(s[0]) else "No")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# なぜかC#版
using System
using System.Linq

public class aa{
    public static void Main(){

        String s = "11112"
        int count = s.Count(c=> c == s[0])

        if (s.Length != count) {
            s = "No"
        }

        Console.WriteLine(s)
    }
}
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D100:区切り文字の統一
s = input()
c1 = s.count('-')
c2 = s.count('_')
if c1 < c2 or c1 == c2:
    s = s.replace('-', '_')
else:
    s = s.replace('_', '-')

print(s)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D090:下一桁はいくつ
# coding: utf-8
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換
n = sum(s)
print(str(n)[-1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D094:犬派か猫派か
# coding: utf-8
s = []
for i in range(3):
    s.append(input())

print("cat" if s.count("cat") > s.count("dog") else "dog")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D108:薬の効き目
# coding: utf-8
import math
n = int(input())
print(str(math.ceil(24 / n)))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D078:入学試験
# coding: utf-8
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換

border = int(input())

avr = sum(s) / len(s)

print("pass" if avr >= border else "failure")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D074:時間の表記
# coding: utf-8
n = int(input())
print(n % 24)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D083:ブラックジャック
# coding: utf-8
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換
n = sum(s)

print("HIT" if n < 16 else "STAND")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D087:文字をくっつける
# coding: utf-8
s = ""
for i in range(int(input())):
    s += input()

print(s)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D087:文字をくっつける
# coding: utf-8
s = input()
print(s[::-1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D097:梅雨入りの予想
# coding: utf-8
s = input().rstrip().split(' ')

print("yes" if s.count('1') >= 5 else "no")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D089:数字の取得
# coding: utf-8
s = input()

ans = ""
for x in s:
    if x.isnumeric():
        ans += x
    else:
        break

print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D110:3つの数字
# coding: utf-8
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換

ans = s[0] * s[1] * s[2]
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D075:足りないカード
# coding: utf-8
s = []
for i in range(4):
    s.append(int(input()))

print(15 - sum(s))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D111:文字を切り詰める
# coding: utf-8
n = int(input())
s = input()
print(s[:n])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D105:長さの一致
# coding: utf-8
s1 = input()
s2 = input()

print("Yes" if len(s1) == len(s2) else "No")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D104:送料の計算
n = int(input())
print(1000 if n < 10 else 150*n)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D107:文字列を囲う
# coding: utf-8
s = input()
s1 = input()

print(s1 + s + s1)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D099:短冊づくり
# coding: utf-8
s = input()
for x in s:
    print(x)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D091:花粉の予報
s = input().rstrip().split(' ')
print(s.count('1') + s.count('2'))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D077:計算機の表示
# coding: utf-8
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換
v = s[0] * s[1]
print(v if v < 10000 else "NG")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D088:温度差の計算
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換

print(s[0] - s[1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D106:割った余り
# coding: utf-8
s = int(input())
s1 = int(input())

print(s % s1)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D102:運賃の計算
# coding: utf-8
s = int(input())
print(100 + s * 10)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D081: 【キャンペーン問題】家族で分ける
# coding: utf-8
f = int(input())
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換

print(s[0] * s[1] % f)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D095:ジュースの分配
s = int(input())
s1 = int(input())

print(s // s1)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D080:忘年会の予算
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換

print(6000 * s[0] + 4000 * s[1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D080:忘年会の予算
s = input().rstrip().split(' ')
s = list(map(int, s))  # 数値変換

print(s[0] * s[1])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C043:使用回数の調査
# coding: utf-8
import collections

n = int(input())
m = input().strip().split(" ")
m = list(map(int, m))   # int変換

c = collections.Counter(m)

mc = c.most_common()

mx = mc[0][1]
l = []

for x in mc:
    if x[1] < mx:
        break
    else:
        l.append(x[0])

l.sort()

print(" ".join([str(x) for x in l]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C030:白にするか黒にするか
# coding: utf-8
s = input().strip().split(" ")
s = list(map(int, s))   # int変換

while True:
    try:
        a = input().strip().split(" ")
        a = list(map(int, a))   # int変換
        print(" ".join([str("1" if x >= 128 else "0") for x in a]))
        
    except EOFError:
        break
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C054:【ぱいじょ！コラボ問題】スピード違反の取り締まり
# coding: utf-8
n = input().strip().split(" ")
n = list(map(int, n))   # int変換

t = []
p = []
while True:
    try:
        a = input().strip().split(" ")
        a = list(map(int, a))   # int変換
        t.append(a[0])
        p.append(a[1])

    except EOFError:
        break

ans = "NO"

for i in range(n[0]):
    if i == 0:
        continue

    if (p[i] - p[i-1]) / (t[i] - t[i-1]) > n[1]:
        ans = "YES"
        break

print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C045:ページネーション
# coding: utf-8
n = input().strip().split(" ")
n = list(map(int, n))   # int変換

x = -(-n[0] // n[1])    # 切り上げ

if x >= n[2]:

    # 配列の作成
    l = []
    for i in range(n[1]):
        a = (i+1) + ((n[2] - 1) * n[1])
        l.append(a)
        if a == n[0]:
            break

    print(" ".join([str(x) for x in l]))

else:
    print("none")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C038:お菓子の分配
n = input().strip().split(" ")
n = list(map(int, n))   # int変換

ans = [0, 1001, 1001]  # No, mod, q

for i in range(n[0]):
    a = int(input())
    m = n[1] % a
    q = n[1] // a

    if (m < ans[1])or (m == ans[1] and q < ans[2]):
        ans[0] = i + 1
        ans[1] = m
        ans[2] = q

print(ans[0])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C031:時差を求めたい
l = {}
for i in range(int(input())):
    a = input().strip().split(" ")
    l[a[0]] = int(a[1])

c = input().strip().split(" ")
name = c[0]
t = c[1].strip().split(":")
t = list(map(int, t))   # int変換

for aa in l.items():
    m = 0
    if l[name] < aa[1]:
        m = aa[1] - l[name]

    else:
        m = l[name] - aa[1]
        m = 24-m

    m = t[0] + m
    
    if m >= 24:
        m -= 24

    print(format(m, '02') + ":" + format(t[1], '02'))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C052:ゲームの画面
w = input().strip().split(" ")
w = list(map(int, w))   # int変換

n = input().strip().split(" ")
n = list(map(int, n))   # int変換

ful = w[0] * w[1]
used = (w[0] - abs(n[0])) * (w[1] - abs(n[1]))

print(ful - used)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D113:初日の出
t = input().strip().split(":")
t = list(map(int, t))   # int変換

x = t[0] - 8

if x < 0:
    x = 24 + x

print(str(x) + ":" + str(t[1]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza D112:工場の生産力
n = int(input())
m = int(input())

print(n * m)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C044:手の組み合わせ
# coding: utf-8
n = int(input())

h = []
for i in range(n):
    h.append(input())

h = sorted(set(h))

if len(h) == 2:
    if h[0] == 'paper':
        if h[1] == 'rock':
            print(h[0])
        else:
            print(h[1])
    else:
        print(h[0])

else:
    print("draw")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# paiza C029:旅行の計画
t = input().strip().split(" ")
t = list(map(int, t))   # int変換

temp = []
for i in range(t[0]):
    a = input().strip().split(" ")
    a = list(map(int, a))   # int変換
    temp.append(a)

h = [x[1] for x in temp]

temp_m = 101
d = [0, 1]

for i in range(t[1]-1, t[0]):
    j = i + 1

    m = sum(h[(j-t[1]):j]) / t[1]

    if m < temp_m:
        temp_m = m
        d = [j-t[1], i]

print(str(temp[d[0]][0]) + " " + str(temp[d[1]][0]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : 荒れ果てた警察署
t = input().strip().split(" ")
t = list(map(int, t))   # int変換

ts = t[0] + t[1]
ans = ts % 10
print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : 荒れ果てたオフィス
n = int(input())

for i in range(n):
    a = input().strip().split(" ")
    if (a[1] == '3'):
        print(a[0])
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : アンドロイドの生産工場
s = input()

ans = ""
for i in range(0, len(s), 2):
    ans += s[i]

print(ans)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : 錆びついた電波塔
n = int(input())
t = input().strip().split(" ")
t = list(map(int, t))   # int変換

print(len([i for i in t if 5 < i]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : お金が引き出せない銀行
n = int(input())
w = int(input())

a = n - w

print("error" if a < 0 else a)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : 荒れ果てたショップ
t = input().strip().split(" ")
t = list(map(int, t))   # int変換

for x in range(t[1], t[2]+1):
    print(str(x).zfill(t[0]))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : 機械の総合病院
s = input()

def f(s):
    if len(s) < 6:
        return "Invalid"

    if s.isdecimal():
        return "Invalid"

    if s.isalpha():
        return "Invalid"

    for i in range(0, len(s)-2):
        ss = s[i:i+3]
        if ss.count(ss[0]) == 3:
            return "Invalid"

    return "Valid"

print(f(s))
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# エンジニアが死滅した世界 : 学べない学校
n = int(input())

a = 0
b = 0

for i in range(n):
    t = input().strip().split(" ")

    if t[0] == t[1] :
        continue
    
    if (t[0] == "g" and t[1] == "c") or \
        (t[0] == "c" and t[1] == "p") or \
        (t[0] == "p" and t[1] == "g"):
        a += 1
    else :
        b += 1

print(a)
print(b)
