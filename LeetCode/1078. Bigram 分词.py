text = "we will we will rock you"
first = "we"
second = "will"

ans = []
t = text.split()

for k, v in enumerate(t):
    if v == first and k <= len(t) - 3:
        if t[k + 1] == second:
            ans.append(t[k + 2])

print(ans)
