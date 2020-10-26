S = "ababcbacadefegdehijhklij"
s = {}
for i in range(len(S)):
    if S[i] in s:
        continue
    n = i
    for j in range(i + 1, len(S)):
        if S[j] == S[i]:
            n = j
    s[S[i]] = n
ans = []
a = 0
start = 0
while a < len(S):
    lst = s[S[a]]
    llst = lst
    for b in range(a, lst):
        if s[S[b]] > lst:
            llst = s[S[b]]
    if llst > lst:
        a = b
    else:
        ans.append(S[start : a + 1])
        start = a + 1
        a = a + 1
print(ans)