import random
import statistics
import math

def root(ids, i):
    while i != ids[i]: i = ids[i]
    return i

def connected(ids, p, q):
    return root(ids, p) == root(ids, q)

def union(ids, size, p, q):
    id1, id2 = root(ids, p), root(ids, q)
    if id1 == id2: return
    if size[id1] <= size[id2]: 
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]

def simulate(n, t):
    p = []
    for _ in range(0, t):
        open = []
        ids = []
        size = []
        top = (n*n)
        bottom = (n*n) + 1
        cnt = 0

        #초기화
        for idx in range(0, (n * n) + 2):
            ids.append(idx)
            size.append(1)
            open.append(0)

        open[top] = 1
        open[bottom] = 1

        for idx in range(0, n):
            union(ids, size, ids[idx], ids[top])

        for idx in range((n * n) - n, (n * n)):
            union(ids, size, ids[idx], ids[bottom])

        while connected(ids, ids[top], ids[bottom]) == False:
            rand = random.randrange(0, (n*n))
            if open[rand] == 1:
                continue

            open[rand] = 1
            cnt += 1
            
            #left
            if rand % n != 0:
                if open[rand - 1] == 1:
                    union(ids, size, ids[rand], ids[rand - 1])
            
            #right
            if (rand +1) % n != 0:
                if open[rand + 1] == 1:
                    union(ids, size, ids[rand], ids[rand + 1])

            #top
            if (rand - n) >= 0:
                if open[rand - n] == 1:
                    union(ids, size, ids[rand], ids[rand - n])

            #bottom
            if (rand + n) < (n*n):
                if open[rand + n] == 1:
                    union(ids, size, ids[rand], ids[rand + n])

        per = float(cnt / (n*n))
        p.append(per)

    m = statistics.mean(p)
    s = statistics.stdev(p)
    interval_start = m - 1.96 * s / math.sqrt(t)
    interval_end = m + 1.96 * s / math.sqrt(t)

    print("mean = %.10f" % (m))
    print("stdev = %.10f" % (s))
    print("95%% confidence interval = [%.10f, %.10f]" % (interval_start, interval_end))

    return m, s