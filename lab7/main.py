import numpy as np
from queue import Queue


def generate(n):
    G = []
    for i in range(n):
        deg = np.random.randint(10, 91)
        range1 = np.arange(i)
        range2 = np.arange(i + 1, n)
        all_range = np.union1d(range1, range2)
        G.append(np.random.choice(all_range, deg, replace=False).tolist())
    for i in range(3):
        for j in range(3, 7):
            if j not in G[i]:
                G[i].append(j)
                G[j].append(i)
    return G


def first(n):
    iters = 0
    G = generate(n)
    u = 0
    q = Queue()
    q.put(u)
    dist = [float('inf')] * n
    dist[u] = 0
    while not q.empty():
        i = q.get()
        for j in G[i]:
            iters += 1
            if dist[j] == float('inf'):
                dist[j] = dist[i] + 1
                q.put(j)
    print(dist)
    print(iters)


def second(n):
    G = generate(n)
    


def main():
    for n in [1000]:
        print('Vertices:', n)
        first(n)
        second(n)


main()
