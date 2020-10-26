s = "cbzxy"
if len(s) == 0 or len(s) == 1:
    print(0)
ans = -1
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            ans = max(ans, j - i - 1)
print(ans)