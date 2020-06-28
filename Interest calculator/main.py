interval_interest = [
    [365.25,0.8],
    [365.25, 0.6],
    [7, 0.6]
    ]
interval_interest.sort()

#subject_dic = {subject: subject_data for subject, subject_data in enumerate(interval_interest)} #dic = [subject_num: [payout_interval, yearly interest]

def subjectPayDay(subject, subject_dic = subject_dic):
    return interval_interest[subject][0]

axis_dic = {subject: [] for subject in range(len(interval_interest))}

start_cash = 1_000_000
duration = 10
day = 0

def cashAfterInterest(subject_id, day = day):
    global start_cash
    global interval_interest
    
    return start_cash*(interval_interest[subject_id][1] + 1)**(day*interval_interest[subject_id][0])

while day < 365.25 * duration:

    for subject in range(len(interval_interest)):
        if subjectPayDay(subject) == subjectPayDay(-1)
        if interval_interest[subject] == interval_interest[-1]:
            day = interval_interest[subject][0]
        if day + interval_interest[subject][0] > interval_interest[subject + 1][0]:
            days_skipped = interval_interest[subject + 1][0] - day
            day = interval_interest[1][0]
        else:
            day = interval_interest[0][0]
        for subject in range(len(interval_interest)):
            if day == interval_interest[subject][0]:
                axis_dic[0].append(cashAfterInterest(0))

    for payout_interval in interval_interest:
        if day == payout_interval:
            start_cash*(interest + 1)**(day * payout_interval)

#"If the graph calculates every day, then "