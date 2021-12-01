with open("1_input.txt") as file:
    data = [int(i) for i in file.readlines()]


"""
Part 1
"""
count = 0

for i, val in enumerate(data, start=1):
    if val > data[i - 2]:
        count += 1

print(f"Part 1: {count}")


"""
Part 2
"""
count = 0
k = 3

# calculate the sum of the first window
prev_sum = sum(data[:k])
curr_sum = 0

for i in range(len(data) - k):
    curr_sum = prev_sum - data[i] + data[i + k]
    if curr_sum > prev_sum:
        count += 1
    prev_sum = curr_sum

print(f"Part 2: {count}")
