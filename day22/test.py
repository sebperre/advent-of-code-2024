from collections import deque

f = open("input.txt")

secret_numbers = []
for line in f:
    secret_numbers.append(int(line))

def next_sec_num(secret_number):
    secret_number = ((secret_number << 6) ^ secret_number) % 16777216
    secret_number = ((secret_number >> 5) ^ secret_number) % 16777216
    secret_number = ((secret_number << 11) ^ secret_number) % 16777216
    return secret_number

diff_money_makes = []

for secret_number in secret_numbers:
    diff_money_make = {}

    prev_secret_number = secret_number
    curr_secret_number = next_sec_num(secret_number)

    secret_number_diffs = deque()

    for _ in range(4):
        secret_number_diffs.append(curr_secret_number % 10 - prev_secret_number % 10)

        prev_secret_number = curr_secret_number
        curr_secret_number = next_sec_num(curr_secret_number)

    for _ in range(1996):
        if tuple(secret_number_diffs) not in diff_money_make:
            diff_money_make[tuple(secret_number_diffs)] = prev_secret_number % 10
        
        secret_number_diffs.popleft()
        secret_number_diffs.append(curr_secret_number % 10 - prev_secret_number % 10)

        prev_secret_number = curr_secret_number
        curr_secret_number = next_sec_num(curr_secret_number)
    
    diff_money_makes.append(diff_money_make)

max_bananas = 0

for i in range(-9, 10):
    print(i)
    for j in range(-9, 10):
        for k in range(-9, 10):
            for l in range(-9, 10):
                curr_bananas = 0
                for seq in diff_money_makes:
                    if (i, j, k, l) in seq:
                        curr_bananas += seq[(i, j, k, l)]
                max_bananas = max(max_bananas, curr_bananas)

print(max_bananas)