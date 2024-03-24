def task1():
    print('Input number of vertices:')
    n = int(input())
    print('Input incidence matrix:')
    i_matrix = []
    for i in range(n):
        row = list(map(int, input().split(' ')))
        i_matrix.append(row)
    a_matrix = [[0] * n for _ in range(n)]
    for i in range(len(i_matrix[0])):
        beg_pos, end_pos = 0, 0
        for j in range(n):
            if i_matrix[j][i] == 1:
                beg_pos = j
            elif i_matrix[j][i] == -1:
                end_pos = j
        a_matrix[beg_pos][end_pos] = 1
    for i in range(n):
        for j in range(n):
            print(a_matrix[i][j], end=' ')
        print()


def task2():
    print('Input number of vertices:')
    n = int(input())
    print('Input weighted graph:')
    weights = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        row = list(map(float, input().split(' ')))
        for j in range(n):
            if row[j] != 0:
                weights[i][j] = row[j]
    for i in range(n):
        for u in range(n):
            for v in range(n):
                weights[u][v] = min(weights[u][v], weights[u][i] + weights[i][v])
    for i in range(n):
        for j in range(n):
            print(weights[i][j], end=' ')
        print()


def main():
    #task1()
    task2()


main()

# 1 1 1 -1 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0
# -1 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 1 0 0 0 -1 0 0 0 -1 0 0 0 0 0
# 0 -1 0 0 0 0 1 1 1 0 -1 0 0 0 0 0 0 -1 0
# 0 0 -1 0 0 0 -1 0 0 1 1 1 0 0 -1 -1 0 0 0
# 0 0 0 0 0 -1 0 0 0 0 0 0 1 1 1 0 0 0 -1
# 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 1 1 0 0
# 0 0 0 0 0 0 0 0 -1 0 0 -1 0 0 0 0 -1 1 1


# 0 19 17 10 13 17 0 0
# 19 0 10 0 0 0 0 0
# 17 10 0 0 18 16.5 0 0
# 10 0 0 0 12 0 10 14.5
# 13 0 18 12 0 16 11 16
# 17 0 16.5 0 16 0 0 19
# 0 0 0 10 11 0 0 14
# 0 0 0 14.5 16 19 14 0
