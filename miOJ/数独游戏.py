line = '5,3,-,6,-,-,-,9,8 -,7,-,1,9,5,-,-,- -,-,-,-,-,-,-,6,- 8,-,-,4,-,-,7,-,- -,6,-,8,-,3,-,2,- -,-,3,-,-,1,-,-,6 -,6,-,-,-,-,-,9,- -,-,-,4,1,9,-,8,- 2,8,-,-,-,5,-,7,9'
line += ' '
list = [[]for i in range(9)]
l = []
b = 0

for j in line:

    if j == ' ':

        list[b].append(a)
        b += 1
    
    elif j == ',':

        list[b].append(a)
    
    else:

        a = j

#判断每一宫
for x in range(9):

    for y in range(9):

        l.append(list[x][y])

    for z in range(1, 10):

        c = str(z)
        if l.count(c) > 1:

            line = 'false'
            break
    
    else:

        l = []
        continue

    break

if line != 'false':

    #判断每一行
    m = 0
    n = 0
    for a in range(3):

        for b in range(3):

            for c in range(3):

                for d in range(3):

                    l.append(list[a + c + m][b + d + n])

            for x in range(1, 10):

                y = str(x)
                if l.count(y) > 1:

                    line = 'false'
                    break
            
            else: 
                
                l = []
                n += 2
                continue

            break
        
        else: 
            
            m += 2
            n = 0
            continue

        break

if line != 'false':

    #判断每一列
    m = 0
    n = 0
    for a in range(3):

        for b in range(3):

            for c in range(3):

                for d in range(3):

                    l.append(list[a + c + m][b + d + n])
                    n += 2

                m += 2
                n = 0

            for x in range(1, 10):

                y = str(x)
                if l.count(y) > 1:

                    line = 'false'
                    break
            
            else: 
                
                l = []
                m = 0
                continue
                
            break

        else: continue
        break

if line != 'false':

    line = 'true'

print(line)