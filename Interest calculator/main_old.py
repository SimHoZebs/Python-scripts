import matplotlib.pyplot as plt

kdb = 1_000_000
kakao = 1_000_000 
kakao_yearly = 1_000_000

kdb_interest = 0.008
kakao_interest = 0.006 / 365.4 * 7
kakao_yearly_interest = 0.006

a_x = []
b_x = []
c_x = []
y = []

day = 0
year = 1

jumped = 0

def acc_num(var):
    return round(var, len(str(int(var))) + 1)

while day < 365.25 * 7:
    print(day)
    
    if jumped != 0:
        day = acc_num(day + 7 - jumped)
        kakao= kakao + kakao*kakao_interest
        jumped = 0
    
    if day + 7 == 365.25 * year:
        kakao = kakao + kakao*kakao_interest
    if day + 7 >= 365.25 * year:
        jumped = 365.25*year - day
        day = acc_num(365.25*year)
        year += 1
        kdb = kdb + kdb*kdb_interest
        kakao_yearly = kakao_yearly + kakao_yearly*kakao_yearly_interest
    else:
        day = day + 7
        kakao = kakao + kakao*kakao_interest    
    
    # print(day)
    a_x.append(kdb)
    c_x.append(kakao_yearly)
    b_x.append(kakao)
    y.append(day/365.25)

print(len(a_x))
print("a", kdb)
print("b", kakao)
print("c", kakao_yearly)

plt.plot(y, a_x)
plt.plot(y, b_x)
plt.plot(y, c_x)

plt.show()




