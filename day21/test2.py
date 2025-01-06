import math
# dict_dirs_arrowpad = {('^', '^'): 'A', ('^', '>'): 'v>A', ('^', '<'): 'v<A', ('^', 'v'): 'vA', ('^', 'A'): '>A', ('>', '^'): '<^A', ('>', '>'): 'A', ('>', '<'): '<<A', ('>', 'v'): '<A', ('>', 'A'): '^A', ('<', '^'): '>^A', ('<', '>'): '>>A', ('<', '<'): 'A', ('<', 'v'): '>A', ('<', 'A'): '>>^A', ('v', '^'): '^A', ('v', '>'): '>A', ('v', '<'): '<A', ('v', 'v'): 'A', ('v', 'A'): '>^A', ('A', '^'): '<A', ('A', '>'): 'vA', ('A', '<'): 'v<<A', ('A', 'v'): '<vA', ('A', 'A'): 'A'}

dict_dirs_arrowpad = {('^', '^'): '', ('^', '>'): 'v>', ('^', '<'): 'v<', ('^', 'v'): 'v', ('^', 'A'): '>', ('>', '^'): '<^', ('>', '>'): '', ('>', '<'): '<<', ('>', 'v'): '<', ('>', 'A'): '^', ('<', '^'): '>^', ('<', '>'): '>>', ('<', '<'): '', ('<', 'v'): '>', ('<', 'A'): '>>^', ('v', '^'): '^', ('v', '>'): '>', ('v', '<'): '<', ('v', 'v'): '', ('v', 'A'): '>^', ('A', '^'): '<', ('A', '>'): 'v', ('A', '<'): 'v<<', ('A', 'v'): '<v', ('A', 'A'): ''}


max_depth = 2
memo = {}

# def dfs(code, depth):
#     if depth == max_depth or code == "":
#         return code
#     if (code, depth) in memo:
#         return memo[(code, depth)]
#     res = ""
#     for i in range(len(code) + 1):
#         if i == 0:
#             res += dfs(dict_dirs_arrowpad[("A", code[i])], depth + 1)
#         elif i == len(code):
#             res += "A" + dfs(dict_dirs_arrowpad[(code[i - 1], "A")], depth + 1)
#         else:
#             res += "A" + dfs(dict_dirs_arrowpad[(code[i - 1], code[i])], depth + 1)
#     memo[(code, depth)] = res
#     return memo[(code, depth)]

def dfs(code, depth):
    if depth == max_depth or code == "":
        return len(code)
    if (code, depth) in memo:
        return memo[(code, depth)]
    res = 0
    for i in range(len(code) + 1):
        if i == 0:
            res += dfs(dict_dirs_arrowpad[("A", code[i])], depth + 1)
        elif i == len(code):
            res += 1 + dfs(dict_dirs_arrowpad[(code[i - 1], "A")], depth + 1)
        else:
            res += 1 + dfs(dict_dirs_arrowpad[(code[i - 1], code[i])], depth + 1)
    memo[(code, depth)] = res
    return memo[(code, depth)]

# code1 = ['A<A^A^^>AvvvA', 'A<A^A^>^AvvvA', 'A<A^A>^^AvvvA']
# code2 = ['A^^^A<AvvvA>A']
# code3 = ['A^<<A^^A>>AvvvA', 'A<^<A^^A>>AvvvA']
# code4 = ['A^^<<A>A>AvvA', 'A^<^<A>A>AvvA', 'A^<<^A>A>AvvA', 'A<^^<A>A>AvvA', 'A<^<^A>A>AvvA']
# code5 = ['A^A^^<<A>>AvvvA', 'A^A^<^<A>>AvvvA', 'A^A^<<^A>>AvvvA', 'A^A<^^<A>>AvvvA', 'A^A<^<^A>>AvvvA', 'A^A<<^^A>>AvvvA']

code1 = ['<A^A^^>Avvv', '<A^A^>^Avvv', '<A^A>^^Avvv']
code2 = ['^^^A<AvvvA>']
code3 = ['^<<A^^A>>Avvv', '<^<A^^A>>Avvv']
code4 = ['^^<<A>A>Avv', '^<^<A>A>Avv', '^<<^A>A>Avv', '<^^<A>A>Avv', '<^<^A>A>Avv']
code5 = ['^A^^<<A>>Avvv', '^A^<^<A>>Avvv', '^A^<<^A>>Avvv', '^A<^^<A>>Avvv', '^A<^<^A>>Avvv', '^A<<^^A>>Avvv']

codes = [code1, code2, code3, code4, code5]
start_codes = ["029A", "980A", "179A", "456A", "379A"]

res = 0

for i, code in enumerate(codes):
    m = math.inf
    for c in code:
        m = min(m, dfs(c, 0) + 1)
    res += int(start_codes[i][0:3]) * m

print(res)
