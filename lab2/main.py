def num1():
    subwords = set()
    word = 'комбинаторика'
    for i in range(13):
        for j in range(13):
            for k in range(13):
                for l in range(13):
                    check = {i, j, k, l}
                    if len(check) == 4:
                        cur_subword = word[i] + word[j] + word[k] + word[l]
                        subwords.add(cur_subword)
    print(len(subwords))


def num2():
    a = [0] * 101
    a[0], a[1] = 5, 6
    for i in range(2, 101):
        a[i] = 7 * a[i - 1] - 12 * a[i - 2]
    print(a[100], 14 * (3**100) - 9 * (4**100))


def num3():
    field = []
    for i in range(16):
        row = [0] * 15
        field.append(row)

    def step(i, j):
        if i == 15 and j == 14:
            return 1
        result = 0
        if i + 1 < 16:
            result += step(i + 1, j)
        if j + 1 < 15:
            result += step(i, j + 1)
        return result

    def cond_step(i, j):
        field[i][j] = 1
        if i == 15 and j == 14:
            return 1
        result = 0
        if i + 1 < 16 and (i == 0 or field[i - 1][j] == 0):
            result += cond_step(i + 1, j)
        if j + 1 < 15:
            result += cond_step(i, j + 1)
        return result

    print(step(0, 0), cond_step(0, 0))


num3()

