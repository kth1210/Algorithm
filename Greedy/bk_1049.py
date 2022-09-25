import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
pack = []
piece = []
price = 0

for _ in range(M):
    P, I = map(int, sys.stdin.readline().split())
    heapq.heappush(pack, P)
    heapq.heappush(piece, I)

packCount = N // 6
pieceCount = N % 6

cheapPack = heapq.heappop(pack)
cheapPiece = heapq.heappop(piece)

if cheapPiece * 6 > cheapPack:
    price += packCount * cheapPack

    if pieceCount * cheapPiece > cheapPack:
        price += cheapPack
    else:
        price += pieceCount * cheapPiece
else:
    price += N * cheapPiece

print(price)