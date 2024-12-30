f = open("input.txt")

content = f.readlines()

a = int(content[0][12:-1])
b = int(content[1][12:-1])
c = int(content[2][12:-1])

operations = [int(x) for x in content[4][9:].split(",")]

op_to_ins = {0: "adv", 1: "bxl", 2: "bst", 3: "jnz", 4: "bxc", 5: "out", 6: "bdv", 7: "cdv"}
combo = ["adv", "bst", "out", "bdv", "cdv"]

output = []

def get_combo_op(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    assert operand != 7

##### Correct #####
i = 0
while i < len(operations):
    match operations[i]:
        case 0:
            a = a // (2 ** get_combo_op(operations[i + 1]))
        case 1:
            b ^= operations[i + 1]
        case 2:
            b = get_combo_op(operations[i + 1]) % 8
        case 3:
            if a != 0:
                i = operations[i + 1]
                i -= 2
        case 4:
            b ^= c
        case 5:
            output.append(str(get_combo_op(operations[i + 1]) % 8))
        case 6:
            b = a // (2 ** get_combo_op(operations[i + 1]))
        case 7:
            c = a // (2 ** get_combo_op(operations[i + 1]))
    i += 2

# print(a, b, c)
print(output)

print(",".join(output))