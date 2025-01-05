import threading

f = open("testinput.txt")

secret_numbers = []
for line in f:
    secret_numbers.append(int(line))

def next_sec_num(secret_number):
    secret_number = ((secret_number << 6) ^ secret_number) % 16777216
    secret_number = ((secret_number >> 5) ^ secret_number) % 16777216
    secret_number = ((secret_number << 11) ^ secret_number) % 16777216
    return secret_number

result = 0

all_secret_numbers = []
differences = []

for secret_number in secret_numbers:
    all_secret_number = []
    difference = []
    for _ in range(2000):
        prev_num = secret_number
        secret_number = next_sec_num(secret_number)
        all_secret_number.append(secret_number % 10)
        difference.append(secret_number % 10 - prev_num % 10)
    all_secret_numbers.append(all_secret_number)
    differences.append(difference)

max_bananas = 0

def find_banana_seq(i, j, k, l):
    
for i in range(-9, 10):
    for j in range(-9, 10):
        for k in range(-9, 10):
            for l in range(-9, 10):
                print(i, j, k, l)
                curr_bananas = 0
                for z, diff in enumerate(differences):
                    p = 0
                    while p < len(diff) - 3:
                        if diff[p] == i and diff[p + 1] == j and diff[p + 2] == k and diff[p + 3] == l:
                            curr_bananas += all_secret_numbers[z][p + 3]
                            break
                        p += 1
                max_bananas = max(curr_bananas, max_bananas)

print(max_bananas)