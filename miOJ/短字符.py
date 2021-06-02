line = 'aa ab'
b = 0
m = ''
n = ''

for a in line:
    
    if a == ' ':

        b = 1
    
    elif b == 0:

        m += a

    else:

        n += a

for i in m:

    line = ''
    if i in n:
        
        n = n.replace(i, '', 1)
        line = 'true'

    else:

        line = 'false'
        break
    
print(line)