#inputText = input().split()
pairList = []

while True:
    try:
        inputPair = [int(num) for num in input().split()]
        pairList.append(inputPair)
    except Exception as e:
        break

def CycleLen(num):
    chainLen = 1
    while num > 1:
        chainLen += 1
        num = num // 2 if num % 2 == 0 else 3*num + 1
    return chainLen

for inputPair in pairList:
    countList = []
    minRange = min(inputPair[0], inputPair[1])
    maxRange = max(inputPair[0], inputPair[1])
    for num in range(minRange, maxRange + 1):
        countList.append(CycleLen(num))

    countList.sort()
    print(inputPair[0], inputPair[1], countList[-1])

print()