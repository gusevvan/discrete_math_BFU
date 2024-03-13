def solve(n, m, g):
    cur_massage = 1
    k = n - m
    max_iter = 2**m
    code_table = {}
    while cur_massage < max_iter:
        temp = cur_massage * (2**k)
        temp_bin = str(bin(temp))[2:].zfill(n)
        rem = temp_bin[:n - m + 1]
        right = m - 1
        while True:
            res_rem = ''
            for i in range(n - m + 1):
                if rem[i] != g[i]:
                    res_rem += '1'
                else:
                    if len(res_rem) > 0:
                        res_rem += '0'
            while right > 0 and len(res_rem) < n - m + 1:
                res_rem += '0'
                right -= 1
            rem = res_rem
            if len(rem) < n - m + 1:
                break
        code_table[temp_bin[:m]] = temp_bin[:m] + rem.zfill(n - m)
        cur_massage += 1
    for key in code_table:
        print(key, code_table[key])
    min_dist = float('inf')
    codes = list(code_table.values())
    for i in range(len(codes)):
        for j in range(len(codes)):
            if i != j:
                diff = 0
                for k in range(n):
                    diff += codes[i][k] != codes[j][k]
                min_dist = min(min_dist, diff)
    print('d_min:', min_dist)
    print('Generative matrix:')
    cur_massage = 1
    while cur_massage < max_iter:
        print(codes[cur_massage - 1])
        cur_massage *= 2

def main():
    solve(31, 11, '101100010011011010101')


main()
