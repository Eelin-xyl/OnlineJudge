num = "112"
k = 1

if k == len(num) or len(num) == 1:
    print("0")

while k > 0:
    i = 0
    while i < len(num) - 1:
        if num[i] > num[i + 1]:
            new = ''
            for a in range(len(num)):
                if a != i:
                    new += num[a]
            num = new
            k -= 1
            break
        elif i + 1 == len(num) - 1:
            num = num[:-1]
            k -= 1
            break
        i += 1
print(str(int(num)))