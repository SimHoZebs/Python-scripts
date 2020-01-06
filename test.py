q_value = 2_000_000
num_list = []
composite_list = []
answer = 0

for num in range(3, q_value + 1, 2):
    num_list.append(num)

for index in range(0, len(num_list)):
    if num_list[index] >= q_value//num_list[index]:
        break

    for multiplier in range(num_list[index], q_value//num_list[index]+1, 2):
        composite_num = num_list[index]*multiplier

        if composite_num >= q_value:
            break

        composite_list.append(composite_num)

num_set = set(num_list)
composite_set = set(composite_list)

set_diff = num_set.difference(composite_set)
result_list = list(set_diff)
result_list.append(2)

for num in result_list:
    answer += num

print(f"Answer = {answer}")