import sys
import time

starttime = time.time_ns()
inf = open('sample_input.txt')

T = inf.readline();

for t in range(0, int(T)):

    N = inf.readline()
    num_list = inf.readline().rstrip().split()

    print(num_list)

    counts = dict()
    for n_list in num_list :
        counts[n_list] = counts.get(n_list, 0) + 1
    xor_list = list()

    for odd_count in counts.keys() :
        if counts[odd_count]%2 == 1 :
            xor_list.append(counts.get(0, odd_count))
    print(xor_list)
    cnt = 0
    Answer = int(xor_list[len(xor_list)-1])
    while cnt < (len(xor_list)-1): # 조건문
        Answer = (int(xor_list[cnt])^Answer)
        cnt += 1

    # Print the answer to standard output(screen).
    print('Case #%d' %(int(t)+1))
    print(Answer)
    print(time.time_ns() - starttime)
inf.close()