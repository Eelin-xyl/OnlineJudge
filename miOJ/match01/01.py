line = '4 2'
n = ''
l = ''
s = 0
result = ''

for i in line:
    
    if i != ' ' and s == 0:
        
        n = n + i
    
    elif i != '' and s == 1:

        l = l + i

    else:

        s = 1;

n = int(n)
l = int(l)

if n - l == 1 or 2 :

    result = 'Impossible'