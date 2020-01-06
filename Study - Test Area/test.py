prime_list = set()
value = 20

for num in range(2, (value//2) + 1):
    print(f"new loop; num is {num}")
    if value % num == 0:
        print(f"{num} is a factor of {value}." )
        value = (value / num)
        print(f"value changing to {value} because num after it aren't factors.")
        if value == 1:
            print(f"Adding {num} to prime_list")
            prime_list.add(num)
            break
        print(f"Check prime in range {(num//2) + 2}")
        for num2 in range(2, (num//2) + 2):
            print(f"Checking if {num} can be divided by {num2}")
            if num % num2 == 0 and num2 != num:
                print(f"It can be divided and it's not {num}, so it's not a prime.")
                break
            else:
                print(f"Adding {num} to prime_list")
                prime_list.add(num)
    else:
        print(f"{num} is not a factor of {value}.")

prime_list = list(prime_list)
prime_list.sort()
print(prime_list[-1])
