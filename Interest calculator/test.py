interval_interest = [[365.25],[365.25],[7]]
interval_interest.sort()

print(interval_interest)

subject_dic = {subject: subject_data for subject, subject_data in enumerate(interval_interest)}

print(subject_dic)