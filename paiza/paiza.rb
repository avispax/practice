line=gets
w1 = line.split(" ")
line=gets
w2 = line.split(" ")

w1a = w1[0].to_f
w1c = w1[1].to_f

w2a = w2[0].to_f
w2c = w2[1].to_f

if ( w1a / w1c > w2a / w2c ) then
    puts w1c.to_i
else
    puts w2c.to_i
end
-------------------

l = gets
a = l.split(" ")
n = a[0].to_i

ans = 0
if ( a[1] == "km" ) then
    ans = n * 1000 * 100 * 10
elsif (a[1] == "m") then
    ans = n * 100 * 10
else
    ans = n * 10
end

puts ans
----------------
while line=gets
    puts line.chomp.upcase
end
-------------------
#paiza D016 N����Ŀ�ޤǳ���

line=gets
w1a = line.to_s
line=gets
w1b = line.to_i

#1���ַֽ�Υ��`��
w1b.times do |i|
    puts w1a[i]
end

#�ޤȤ�Ʊ�ʾ�Υ��`��
s = ""
w1b.times do |i|
    s += w1a[i]
end
puts s

#�ޤȤ��2 n����Ŀ����m�����ʾ
puts w1a[0, w1b]
-------------------
#paiza D017 ������С
arr = [0, 0, 0, 0, 0]
i = 0
while line = gets
    arr[i] = line.to_i
    i = i + 1
end

puts arr.max
puts arr.min
-------------------
#paiza D019 �����Ф���N��Ŀ
l = gets
a = l.split(" ")
s = a[0].to_s
n = a[1].to_i

puts s[n-1]
-------------------
#paiza D021 �����Ф�һ��
line = gets
s1 = line.to_s
line = gets
s2 = line.to_s

puts s1 == s2 ? "Yes" : "No"
-------------------
#paiza D022 ����e��Ӌ��
line = gets
n = line.to_i

puts 6 * n * n
-------------------
#paiza D023 A�΂���
line = gets
s1 = line.to_s

puts s1.count('A')
-------------------
#paiza D024 �����Τ��ڽǤκ�
line = gets
n1 = line.to_i
line = gets
n2 = line.to_i

puts 180 - n1 - n2
-------------------
#paiza D025 ���֤γ���
line = gets
n = line.to_i

puts format("%03d", n)
-------------------
#paiza D026 һ�L�g���趨
n = 0
while line=gets
    s = line.chomp
    if s == "no" then
        n = n + 1
    end
end
puts n
-------------------
#paiza D027 n�ޤǤκ�
line = gets
n = line.to_i

puts (n * (n + 1)) / 2
-------------------
#paiza D028 ���֤�����
line = gets
n = line.chomp

puts n.size
-------------------
#paiza D029 ����������Y��
line = gets
n = line.to_i

puts 7 - n
-------------------
#paiza D031 �֤������ 
line = gets
n = line.to_i

puts n * 60
-------------------
#paiza D032 ��늕r�g

line = gets
n = line.to_i

puts 100 - n
-------------------
#paiza D033 �^����
line = gets
a = line.split(" ")
s1 = a[0].to_s
s2 = a[1].to_s

puts s1[0] + "." + s2[0]
-------------------
#paiza D034 �ɤ�ˤ��褦����
line = gets
n = line.to_i

ans = 21 % n

puts ans == 0 ? n : ans
-------------------
#paiza D035 �ո��Υǩ`��
line = gets
a = line.split(" ")

puts a[0].to_s + "/" + a[1].to_s + "/" + a[2].to_s
-------------------
#paiza D036 ���åȥީ`�� : �ÓQ
line = gets
s = line.to_s

puts s.gsub("at", "@")
-------------------
#paiza D037 ����֢�ǤĤ餤
line = gets
n1 = line.to_i
line = gets
n2 = line.to_i

m = n2.divmod(n1)

puts m[1] > 0 ? m[0] + 1 : m[0]
-------------------
#paiza D041 �����x��
line = gets
a = line.split(" ")

n1 = a[0].to_i
n2 = a[1].to_i
n3 = a[2].to_i

puts n2 * n3 > n1 ? "OK" : "NG"
-------------------
#paiza D038 ԇ�Ϥλ���
line = gets
n = line.to_i

puts n * (n - 1) /2
-------------------
#paiza D039 �������Τ��ɤ���
line = gets
s1 = line.to_i
line = gets
s2 = line.to_i
line = gets
s3 = line.to_i

puts (s1 == s2 && s2 == s3) ? "OK" : "NG"
-------------------
#paiza D040 �B�ݤ����
cnt = 0
while line=gets
    n = line.to_i
    if n <= 30 then
        cnt = cnt + 1
    end
end
puts cnt
-------------------
#paiza D042 ����
line = gets
n = line.split(" ")
a = n[0].to_i
b = n[1].to_i

line = gets
n = line.split(" ")
c = n[0].to_i
d = n[1].to_i

puts a * d - b * c
-------------------
#paiza D043 ��ݤα�ʾ
line=gets
n = line.to_i

s = ""
if n >= 0 && n <= 30 then
	s = "sunny"
elsif n >= 31 && n <= 70 then
	s = "cloudy"
else
	s = "rainy"
end

puts s
-------------------
#paiza D044 �Ϥ���ޤ���
line = gets
n = line.split(" ")
s1 = n[0].to_s
s2 = n[1].to_s

s = ""
if s2 == "M" then
    s = "Hi, Mr. " + s1
else
    s = "Hi, Ms. " + s1
end

puts s
-------------------
#paiza D045 ֪ͨƱ
line=gets
n = line.to_i

s=""
case n
when 5 then
  s = "A"
when 4 then
  s = "B"
when 3 then
  s = "C"
when 2 then
  s = "D"
when 1 then
  s = "E"
end

puts s

#����2
line=gets
n = line.to_i

hash = {5 => "A", 4 => "B", 3 => "C", 2 => "D", 1 => "E"}

puts hash[n]
-------------------
#paiza D047 ����ꥹ�Ȥα�ʾ
line = gets
s1 = line.to_s
line = gets
s2 = line.to_s
line = gets
s3 = line.to_s

puts "Gold " + s1
puts "Silver " + s2
puts "Bronze " + s3
-------------------
#paiza D046 ��˼�h�ʥ��ޥ�
line = gets
n = line.split(" ")

puts n.max
-------------------
#paiza D048 ̨�L���g��
arr = [0, 0, 0, 0, 0]
i = 0
while line = gets
    arr[i] = line.to_i
    i = i + 1
end

4.times do |i|
    puts (arr[i+1] - arr[i])
end
-------------------
#paiza D049 xx����
line = gets
s = line.to_s

puts s.gsub("noaki", "")
-------------------
#paiza D050 ����Ҋ����
line = gets
n = line.split(" ")
a1 = n[0].to_i
a2 = n[1].to_i

if a1 >= 5 then
	a1 = 5
end

if a2 >= 5 then
	a2 = 5
end

puts a1 + a2
