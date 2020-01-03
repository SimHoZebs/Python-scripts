##### Problem 1
```python
sum_num = 0

for num in range(0,1000):
    if num % 3 == 0 or num % 5 == 0:
        sum_num += num

print(sum_num)

#5 lines
```

#####Problem 2
```python
value1 = 1
value2 = 1
alist = []
result = 0

while value1 < 4000000 or value2 < 4000000:
    value1 += value2
    alist.append(value1)
    value2 += value1
    alist.append(value2)

for num in alist:
    if num % 2 == 0 and num < 4000000:
        result += num

print(result)

#13 lines
```

#####Problem 3
```python
prime_list = set()
value = 600851475143

for num in range(2, (value//2) + 1):
    if value % num == 0:
        #print(f"{num} is a factor of {value}." )
        value = (value / num)
        #print(f"value changing to {value} because num after it aren't factors.")
        #print(f"Check prime in range {(num//2) + 2}")
        if value == 1:
            #print(f"Adding {num} to prime_list")
            prime_list.add(num)
            break
        for num2 in range(2, (num//2) + 2):
            #print(f"Checking if {num} can be divided by {num2}")
            if num%num2 == 0 and num2 != num:
                #print(f"It can be divided and it's not {num}, so it's not a prime.")
                break
            else:
                #print(f"Adding {num} to prime_list")
                prime_list.add(num)
    else:
        #print(f"{num} is not a factor of {value}.")

prime_list = list(prime_list)
prime_list.sort()            
print(prime_list[-1])

#15 lines

#Below is an alternate answer. Only true because of the question's specific value.

prime_list = []
value = 600851475143

for num in range(2, (value + 1) // 2):
    if value == 1:
        break
    if value % num == 0:
        value = (value / num)
        prime_list.append(num)

print(prime_list[-1])

#9 lines
```

#####Problem 4
```python
list_pali = []
pali_num = 1

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        #print(f"Multiplying {num1} with {num2}")
        result = num1 * num2
        #print(f"Got {result}. Checking for palidrome")
        pali_check = list(str(result))
        #print(f"pali_check list is: {pali_check}")
        #print(f"Checking from 0 to {len(pali_check)}")
        for place in range (0, len(pali_check)):
            #print(f"comparing placement {place} and {-(place +1)}")
            if pali_check[place] != pali_check[-(place + 1)]:
                #print("They are not the same!")
                break
            if place == len(pali_check) - 1:
                #print(f"{result} is the largest palidrome for {num1}!")
                list_pali.append(result)
                break
        if len(list_pali) == pali_num:
            pali_num += 1
            break

list_pali.sort()
print(list_pali[-1])

#17 lines
```

#####Problem 5
```python
maxnum = 20
numlist = []
rem = []
fac = []

divider = 2
wasdivided = None
answer = 1

for num in range(maxnum//2, maxnum +1):
    numlist.append(num)

while divider != maxnum//2:
    for num in numlist:
        #print(f"dividing {num} with {divider}")
        
        if num//2 < divider and num != divider:
            #print(f"{num} isn't worth trying to divide by {divider}.")
            rem.append(num)
               
        elif num % divider == 0:
            #print(f"{num} can be divided by {divider}!"
            #       f"\nDividing then putting {num//2} in rem")
            rem.append(num//divider)
            wasdivided = True
                
        elif num % divider != 0:
            #print(f"{num} can't be divided by {divider}."
            #       f"Putting {num} in rem.")
            rem.append(num)
    
    #print(f"rem: {rem}")
    if wasdivided:
        fac.append(divider)
        wasdivided = 0
    elif not wasdivided:
        divider += 1
        
    numlist = rem.copy()
    #print(f"numlist: {numlist}")
    rem = []

for _ in fac:
    answer *= _
for _ in numlist:
    answer *= _

print(answer)
```

#####Problem 6
```python
made_list = []

def make_list(num):
    global made_list
    
    for _ in range(1, num +1):
        made_list.append(_)

make_list(100)

res1 = 0
for num in made_list:
    res1 += num**2
    
res2 = 0
for num in made_list:
    res2 += num

res2 = res2**2

print(res2 - res1)
```

#####Problem 7
```python
enum = 1

prime_place = 1

primelist = []
result = 0

while prime_place != 10_001:
    #print(f"Testing {enum}")
    if enum == 1:
        enum += 1
    else:
        for num in range(2, enum + 1):
            #print(f"{enum} / {num}")
            if enum % num == 0:
                enum += 1
                break
            
            elif num >= (enum +1)//2:
                #print(f"{enum} is a prime")
                primelist.append(enum)
                result = enum
                prime_place += 1
                enum += 1
                break
                
print(result)
```

#####Problem 8
```python
thelist = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

compared_result = 1

for pos in range(0, len(thelist)):

    multipliers = thelist[pos : pos + 13]

    if '0' in multipliers:
        continue

    for num in multipliers:
        compared_result *= int(num)
    
    if compared_result > result:
        result = compared_result
    
    compared_result = 1

print(result)
```