n = 0
highest_chain_starter = 0

while n < 1_000_000:
    collatz_list = []
    n += 1
    collatz_list.append(n)
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n + 1

    collatz_list.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        collatz_list.append(n)

    chain_len = len(collatz_list)
    print(chain_len)
    highest_chain_starter = n if chain_len > highest_chain_starter else highest_chain_starter

print(highest_chain_starter)