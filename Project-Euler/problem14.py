import matplotlib.pyplot as plt
import numpy as np

test_no = 1
chain = []
chain_len = 0
interval_len = 0

pltpoint_x = []
pltpoint_y = []

while test_no < 10_000:
    test_no += 1
    val = test_no
    pltpoint_x.append(test_no)
    # print("test_no", test_no)

    while val != 1:
        if val%2 == 0:
            val//=2
        else:
            val = 3*val + 1
        chain.append(val)
    print("this val's chain", len(chain))
    pltpoint_y.append(len(chain))
    if chain_len >= len(chain):
        interval_len += 1
    else:
        chain_len = len(chain)
        # print("Interval is ", interval_len)
        interval_len = 0
        chain.clear()

fig, ax = plt.subplots()
ax.plot(pltpoint_x, pltpoint_y)

print(chain_len)

plt.show()