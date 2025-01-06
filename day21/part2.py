from collections import deque
f = open("input.txt")

codes = []

for line in f:
    codes.append(line.strip())

numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
arrowpad = [["#", "^", "A"], ["<", "v", ">"]]

dict_dirs_numpads = {}
dict_dirs_arrowpad = {}

all_keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A"]
arrowpad_keys = ["^", ">", "<", "v", "A"]

def bfs(start, end, region):
    for i in range(len(region)):
        for j in range(len(region[0])):
            if region[i][j] == start:
                start_pos = (i, j)
    
    queue = deque()
    queue.append((start_pos, ""))

    found_shortest = False
    curr_short_len = None
    ret_list = []

    while queue:
        node, seq = queue.popleft()
        
        if region[node[0]][node[1]] == end:
            if not found_shortest:
                found_shortest = True
                curr_short_len = len(seq)
                ret_list.append(seq + "A")
            elif curr_short_len == len(seq):
                ret_list.append(seq + "A")

        if not found_shortest:
            if node[0] + 1 < len(region) and (node[0] + 1, node[1], "v") and region[node[0] + 1][node[1]] != "#":
                queue.append(((node[0] + 1, node[1]), seq + "v"))
            if 0 <= node[0] - 1 and 0 <= node[0] and (node[0] - 1, node[1], "^") and region[node[0] - 1][node[1]] != "#":
                queue.append(((node[0] - 1, node[1]), seq + "^"))
            if node[1] + 1 < len(region[0]) and (node[0], node[1] + 1, ">") and region[node[0]][node[1] + 1] != "#":
                queue.append(((node[0], node[1] + 1), seq + ">"))
            if 0 <= node[1] - 1 and (node[0], node[1] - 1, "<") and region[node[0]][node[1] - 1] != "#":
                queue.append(((node[0], node[1] - 1), seq + "<"))
    return ret_list
    
def create_dict_numpads():
    for s in all_keys:
        for d in all_keys:
            if s == d:
                dict_dirs_numpads[(s, d)] = "A"
            else:
                dict_dirs_numpads[(s, d)] = bfs(s, d, numpad)

def create_dict_arrowpad():
    for s in arrowpad_keys:
        for d in arrowpad_keys:
            if s == d:
                dict_dirs_arrowpad[(s, d)] = "A"
            else:
                dict_dirs_arrowpad[(s, d)] = bfs(s, d, arrowpad)

create_dict_numpads()
create_dict_arrowpad()

print(dict_dirs_arrowpad)

dict_dirs_arrowpad = {('^', '^'): 'A', ('^', '>'): 'v>A', ('^', '<'): 'v<A', ('^', 'v'): 'vA', ('^', 'A'): '>A', ('>', '^'): '<^A', ('>', '>'): 'A', ('>', '<'): '<<A', ('>', 'v'): '<A', ('>', 'A'): '^A', ('<', '^'): '>^A', ('<', '>'): '>>A', ('<', '<'): 'A', ('<', 'v'): '>A', ('<', 'A'): '>>^A', ('v', '^'): '^A', ('v', '>'): '>A', ('v', '<'): '<A', ('v', 'v'): 'A', ('v', 'A'): '>^A', ('A', '^'): '<A', ('A', '>'): 'vA', ('A', '<'): 'v<<A', ('A', 'v'): '<vA', ('A', 'A'): 'A'}

def dfs_numpad(i, curr, code, ans):
    if i == len(code):
        ans.append(curr)
        return
    for seq in dict_dirs_numpads[(code[i - 1], code[i])]:
        dfs_numpad(i + 1, curr + seq, code, ans)

def process_numpad(code):
    results = []
    dfs_numpad(1, "", code, results)
    return results

def process_dirpad(codes):
    shortest = []

    for code in codes:
        res = ""
        for i in range(1, len(code)):
            res += dict_dirs_arrowpad[(code[i - 1], code[i])]
        if not shortest or len(res) < len(shortest[0]):
            shortest = [res]
        else:
            shortest.append(res)
    
    return shortest

# def process_dirpad(codes):
#     results = []
#     shortest = None

#     def dfs_dirpad(i, curr, code, ans):
#         nonlocal shortest
#         if shortest and len(curr) > shortest:
#             return
#         if i == len(code):
#             if not shortest:
#                 shortest = len(curr)
#                 ans.append(curr)
#             elif len(curr) < shortest:
#                 shortest = len(curr)
#                 ans.clear()
#                 ans.append(curr)
#             elif len(curr) == shortest:
#                 ans.append(curr)
#             return
#         for seq in dict_dirs_arrowpad[(code[i - 1], code[i])]:
#             dfs_dirpad(i + 1, curr + seq, code, ans)
#     for code in codes:
#         dfs_dirpad(1, "", code, results)
#     return results

def process_code(code):
    code = "A" + code

    arrowpad1_to_arrowpad2 = ["A" + pos for pos in process_numpad(code)]

    for i in range(24):
        print(i)
        arrowpad1_to_arrowpad2 = ["A" + pos for pos in process_dirpad(arrowpad1_to_arrowpad2)]
        if (i==6):
            print(arrowpad1_to_arrowpad2)
        # print(arrowpad1_to_arrowpad2[0])

    arrowpad2_to_humaninput = process_dirpad(arrowpad1_to_arrowpad2)

    return len(arrowpad2_to_humaninput[0])

res = 0

for code in codes:
    res += int(code[0:3]) * process_code(code)

print(res)


