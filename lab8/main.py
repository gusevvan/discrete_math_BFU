import math
from random import randint


def get_max_vertex(k, V, S):
    m = 0   # наименьшее допустимое значение
    v = -1
    for i, w in enumerate(V[k]):
        if i in S:
            continue

        if w[2] == 1:   # движение по стрелке
            if m < w[0]:
                m = w[0]
                v = i
        else:           # движение против стрелки
            if m < w[1]:
                m = w[1]
                v = i

    return v


def get_max_flow(T):
    w = [x[0] for x in T]
    return min(*w)


def updateV(V, T, f):
    for t in T:
        if t[1] == -1:  # это исток
            continue

        sgn = V[t[2]][t[1]][2]  # направление движения

        # меняем веса в таблице для (i,j) и (j,i)
        V[t[1]][t[2]][0] -= f * sgn
        V[t[1]][t[2]][1] += f * sgn

        V[t[2]][t[1]][0] -= f * sgn
        V[t[2]][t[1]][1] += f * sgn


def fordFulkerson(V, mapper):
    N = len(V)  # число вершин в графе
    init = 0    # вершина истока (нумерация с нуля)
    end = N - 1     # вершинстока
    Tinit = (math.inf, -1, init)      # первая метка маршруто (a, from, vertex)
    f = []      # максимальные потоки найденных маршрутов
    pathes = []
    j = init
    last_S = []
    while j != -1:
        k = init  # стартовая вершина (нумерация с нуля)
        T = [Tinit]  # метки маршрута
        S = {init}  # множество просмотренных вершин

        while k != end:     # пока не дошли до стока
            j = get_max_vertex(k, V, S)  # выбираем вершину с наибольшей пропускной способностью
            if j == -1:         # если следующих вершин нет
                if k == init:      # и мы на истоке, то
                    break          # завершаем поиск маршрутов
                else:           # иначе, переходим к предыдущей вершине
                    k = T.pop()[2]
                    continue

            c = V[k][j][0] if V[k][j][2] == 1 else V[k][j][1]   # определяем текущий поток
            T.append((c, j, k))    # добавляем метку маршрута
            S.add(j)            # запоминаем вершину как просмотренную

            if j == end:    # если дошди до стока
                f.append(get_max_flow(T))     # находим максимальную пропускную способность маршрута
                updateV(V, T, f[-1])        # обновляем веса дуг
                break

            k = j
        last_S = S
        pathes.append(T)
    pathes.pop()
    F = sum(f)
    print(f"Максимальный поток равен: {F}")
    print('Пути потоков:')
    for i, path in enumerate(pathes):
        print(f'Величина потока: {f[i]}')
        print(f'Путь:', end=' ')
        prev = False
        for j in range(1, len(path[1:]) + 1):
            if V[path[j][1]][path[j][2]][2] != -1:
                prev = True
            else:
                if not prev:
                    print(mapper[path[j][2]]    , end=' ')
                prev = False
        print(mapper[N - 1])
    print('Минимальный разрез:')
    print('A:', end=' ')
    for i in range(N):
        if i in last_S:
            print(mapper[i], end=' ')
    print()
    print('B:', end=' ')
    for i in range(N):
        if i not in last_S:
            print(mapper[i], end=' ')
    print()

def findMinCut(V, maxFlow, mapper):
    max_iter = 2**(len(V) - 2)
    for i in range(max_iter):
        cur_bin = '0' + bin(i)[2:].zfill(len(V) - 2) + '1'
        cur_c = 0
        for i in range(len(V)):
            for j in range(len(V)):
                if cur_bin[i] != cur_bin[j] and V[i][j][0] != 0 and V[i][j][2] != -1:
                    if cur_bin[i] == '0':
                        cur_c += V[i][j][0]
                    else:
                        cur_c -= V[i][j][0]
        if cur_c == maxFlow:
            A, B = [], []
            for i in range(len(V)):
                if cur_bin[i] == '0':
                    A.append(mapper[i])
                else:
                    B.append(mapper[i])
            print('Минимальный поток:')
            print('A:', A)
            print('B:', B)
            break
def main():
    mapper = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'T'}
    print('Заданный граф:')
    V = [[[0, 0, 1], [14, 0, 1], [12, 0, 1], [31, 0, 1], [29, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[14, 0, -1], [0, 0, 1], [0, 0, 1], [37, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[12, 0, -1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [27, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[31, 0, -1], [37, 0, -1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [30, 0, 1], [23, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[29, 0, -1], [0, 0, 1], [27, 0, -1], [0, 0, 1], [0, 0, 1], [28, 0, 1], [31, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [30, 0, -1], [28, 0, -1], [0, 0, 1], [0, 0, 1], [16, 0, 1], [15, 0, 1],
          [0, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [23, 0, -1], [31, 0, -1], [0, 0, 1], [0, 0, 1], [22, 0, 1], [20, 0, 1],
          [0, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [16, 0, -1], [22, 0, -1], [0, 0, 1], [14, 0, 1],
          [26, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [15, 0, -1], [20, 0, -1], [14, 0, -1], [0, 0, 1],
          [25, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [26, 0, -1], [25, 0, -1],
          [0, 0, 1]]
         ]
    fordFulkerson(V, mapper)
    V = [[[0, 0, 1], [14, 0, 1], [12, 0, 1], [31, 0, 1], [29, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[14, 0, -1], [0, 0, 1], [0, 0, 1], [37, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[12, 0, -1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [27, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[31, 0, -1], [37, 0, -1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [30, 0, 1], [23, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[29, 0, -1], [0, 0, 1], [27, 0, -1], [0, 0, 1], [0, 0, 1], [28, 0, 1], [31, 0, 1], [0, 0, 1], [0, 0, 1],
          [0, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [30, 0, -1], [28, 0, -1], [0, 0, 1], [0, 0, 1], [16, 0, 1], [15, 0, 1],
          [0, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [23, 0, -1], [31, 0, -1], [0, 0, 1], [0, 0, 1], [22, 0, 1], [20, 0, 1],
          [0, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [16, 0, -1], [22, 0, -1], [0, 0, 1], [14, 0, 1],
          [26, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [15, 0, -1], [20, 0, -1], [14, 0, -1], [0, 0, 1],
          [25, 0, 1]],
         [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [26, 0, -1], [25, 0, -1],
          [0, 0, 1]]
         ]
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            if V[i][j][0] != 0:
                val = randint(100, 1001)
                V[i][j][0] = val
                V[j][i][0] = val
    print('Граф со случайными весами ребер:')
    fordFulkerson(V, mapper)
main()