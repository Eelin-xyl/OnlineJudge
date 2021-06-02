line = '3,3,1,3,4;5,5,7,10,1;2,9,5,3,3'
line += ';'
x = ''
y = []
z = []

for i in line:
    
    if i == ',':

        x = int(x)
        y.append(x)
        x = ''

    elif i == ';':

        x = int(x)
        y.append(x)
        z.append(y)
        x = ''
        y = []

    else:

        x += i

a = 0
b = 0
c = 0
d = 0
s = 0

for m in range(len(z) - 1):

    for n in range(len(z[0]) - 1):

        a = z[m][n]
        d = z[m + 1][n + 1]

        if a + d >= s:

            s = a + d

print(s)