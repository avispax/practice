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
# 1行づつ無限input : break必須
l = []
while True:
    try:
        l.append(int(input().strip()))
    except EOFError:
        break
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
if len(s) == s.count(s[0]):
    print("NG")
else:
    print("OK")
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

if len(s) == s.count(s[0]):
    print(s)
else:
    print("No")
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# なぜかC#版
using System;
using System.Linq;

public class aa{
    public static void Main(){

        String s = "11112";
        int count = s.Count(c => c == s[0]);
        
        if ( s.Length != count ) {
            s = "No";
        }
        
        Console.WriteLine(s);        
    }
}
http: // skywing.hatenablog.com/entry/2018/06/09/095645
