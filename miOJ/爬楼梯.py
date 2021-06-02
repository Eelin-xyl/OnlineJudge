line = 5
list = []
sum = 0

for x in range(0, line):
    
    y = (line - x) / 2
    print(type(y), y)
    
    if y % 1 == 0:
        y = int(y)        
        z = x + y
        m = 1
        n = 1

        for i in range(z - x + 1, z + 1):
        
            m *= i
    
        for j in range(1, x + 1):

            n *= j

        list.append(m / n)

for a in list:

    sum += a

print(int(sum) + 1)