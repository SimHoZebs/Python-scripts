ainput = [int(num) for num in input().split()]

def FindCycleLen(num):
    chainList = [num]
    while num > 1:
        chainList.append(num//2 if num % 2 == 0 else 3*num + 1)
        num = chainList[-1]
    return len(chainList)

minRange = min(ainput[0], ainput[1])
maxRange = max(ainput[0], ainput[1])

countList = []
for num in range(minRange, maxRange + 1):
    countList.append(FindCycleLen(num))

countList.sort()
print(ainput[0], ainput[1], countList[-1])
