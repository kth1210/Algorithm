import random
import statistics

ids = []
size = []
p = []

def root(i):
    while i != ids[i]: i = ids[i]
    return i

def connected(p, q):
    return root(p) == root(q)

def union(p, q):    
    id1, id2 = root(p), root(q)
    if id1 == id2: return
    if size[id1] <= size[id2]: 
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]

def simulate(n, t):
    for _ in range(0, t):
        open = []
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
            union(ids[idx], ids[top])

        for idx in range((n * n) - n, (n * n)):
            union(ids[idx], ids[bottom])


        while connected(ids[top], ids[bottom]) == False:
            rand = random.randrange(0, (n*n))
            if open[rand] == 1:
                continue

            open[rand] = 1
            cnt = cnt + 1
            
            #left
            if rand % n != 0:
                if open[rand - 1] == 1:
                    union(ids[rand], ids[rand - 1])
            
            #right
            if (rand +1) % n != 0:
                if open[rand + 1] == 1:
                    union(ids[rand], ids[rand + 1])

            #top
            if (rand - n) >= 0:
                if open[rand - n] == 1:
                    union(ids[rand], ids[rand - n])

            #bottom
            if (rand + n) < (n*n):
                if open[rand + n] == 1:
                    union(ids[rand], ids[rand + n])

        per = float(cnt / (n*n))

        p.append(per)

        ids.clear()
        open.clear()


    m = statistics.mean(p)
    s = statistics.stdev(p)

    return m, s


'''
Unit Test
'''
if __name__ == "__main__":
    print(simulate(200, 100))