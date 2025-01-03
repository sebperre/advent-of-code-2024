f = open("input.txt")

secret_numbers = []
for line in f:
    secret_numbers.append(int(line))

def next_sec_num(secret_number):
    secret_number = ((secret_number << 6) ^ secret_number) % 16777216
    secret_number = ((secret_number >> 5) ^ secret_number) % 16777216
    secret_number = ((secret_number << 11) ^ secret_number) % 16777216
    return secret_number

result = 0

for secret_number in secret_numbers:
    for _ in range(2000):
        secret_number = next_sec_num(secret_number)
    result += secret_number

print(result)