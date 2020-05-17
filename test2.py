import matplotlib.pyplot as plt

class Euler:

    def __init__(self):
        self.q_val = 0
        self.chain = []
        self.chain_len_list = []
        self.prev_chain_len = 0

        self.prev_chain_len_list = []
        self.x_list = []
        self.y_list = []

    def numProcessing(self, num):
        self.chain.append(num)
        while num != 1:
            if num < self.q_val:
                break




            if num % 2 == 0:
                num //= 2
            else:
                num = 3*num + 1
            self.chain.append(num)
    
    def generate_axis(self, qchain):
        self.prev_chain_len_list.append(len(qchain))
        # print("Append", len(self.chain))

    def plotting(self, a_list):
        for x,y in enumerate(a_list):
            self.x_list.append(x + 1)
            self.y_list.append(y)

        plt.plot(self.x_list, self.y_list)
        pass

q = Euler()
ans_found = False

# while not ans_found:
if __name__ == "__main__":
    while q.q_val != 1000:
        q.q_val += 1
        # print("Testing num:", q.q_val)
        q.numProcessing(q.q_val)
        q.generate_axis(q.chain)

        curr_chain_len = len(q.chain)
        q.chain_len_list.append(curr_chain_len)
        if q.prev_chain_len != 0 and q.prev_chain_len >= curr_chain_len:
            ans_found = True
            ans = curr_chain_len
            # break
        else:   #If curr chain len is 0 or is smaller than new chain's len 
            q.prev_chain_len = curr_chain_len
        q.chain.clear()

    q.plotting(q.prev_chain_len_list)
    plt.show()
    print("Answer", ans)