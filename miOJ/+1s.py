import re

line = '2d06 05 43'

matchObj = re.match(r'(.*?)d(.*?) (.*?) (.*?)', line, re.M|re.I)

a = matchObj.group(0)
d = matchObj.group(1)
h = int(matchObj.group(2))
m = int(matchObj.group(3))
#s = int(matchObj.group(4))

print(a)
print(d)
print(h)
print(m)
#print(s)