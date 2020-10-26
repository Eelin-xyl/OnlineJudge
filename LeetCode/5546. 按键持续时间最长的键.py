releaseTimes = [9,29,49,50]
keysPressed = "cbcd"

mx = releaseTimes[0]
n = [0]
for i in range(1, len(releaseTimes)):
    if releaseTimes[i] - releaseTimes[i - 1] > mx:
        mx = releaseTimes[i] - releaseTimes[i - 1]
        n = [i]
        continue
    if releaseTimes[i] - releaseTimes[i - 1] == mx:
        print(releaseTimes[i])
        n.append(i)

key = []
for i in n:
    key.append(keysPressed[i])
print(max(key))