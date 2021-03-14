p = [1,4,1]
s = [1,5,1]

# big car can hold more people, so sort lists and reverse them.
s.sort()
s.reverse()

# figure out the totle num of people, then count the num of car(form big to small)
sm = sum(p)
n = 0
for i in range(len(s)):
    n += s[i]
    if n >= sm:
        # if got all the people, then do not need more car
        print(i + 1)
        break
# make sure that loop return value, give the max
print(len(s))