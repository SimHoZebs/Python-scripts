interval_interest = [
    [365.25,0.008],
    [365.25, 0.006],
    [7, 0.006],
    [30.5, 0.02]
    ]
interval_interest.sort()

start_cash = 1_000_000

iteration = {subject: 1 for subject in range(len(interval_interest))}
axis_dic = {subject: [[0],[start_cash]] for subject in range(len(interval_interest))}

def subjectPayDay(subject):
    global interval_interest

    return interval_interest[subject][0]

def subjectInterest(subject):
    global interval_interest 

    return interval_interest[subject][1]

def cashAfterInterest(subject):
    global iteration, start_cash, interval_interest
    
    return start_cash * ((subjectInterest(subject) * subjectPayDay(subject))/365.25 + 1)**iteration[subject]

duration = 7
day = subjectPayDay(0)
days_skipped = 0

while day < 365.25 * duration:
    print(day)
    for subject in range(1, len(interval_interest)):

        if days_skipped > 0:
            day += subjectPayDay(0) - days_skipped
            days_skipped = 0
            break

        if day + subjectPayDay(0) < subjectPayDay(subject) * iteration[subject]:
            if subject != len(interval_interest) - 1:
                continue
            day = subjectPayDay(0) * iteration[0]
            break
        else:
            days_skipped = subjectPayDay(subject) * iteration[subject] - day
            day = subjectPayDay(subject) * iteration[subject]
            break

    for subject in range(len(interval_interest)):
        if day % subjectPayDay(subject) == 0:
            axis_dic[subject][0].append(day/365.25)
            axis_dic[subject][1].append(cashAfterInterest(subject))
            iteration[subject] += 1
        else:
            axis_dic[subject][0].append(day/365.25)
            axis_dic[subject][1].append(axis_dic[subject][-1][-1])

import matplotlib.pyplot as plt

for subject in axis_dic:
    plt.plot(axis_dic[subject][0], axis_dic[subject][1])

plt.show()