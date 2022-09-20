import math

def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False


def grahamScan(points):
    angle = []
    result = []
    sor = sorted(points, key = lambda x : (x[1], -x[0]))
    P = sor[0]
    count = len(points)

    for i in range(0, count):
        angle.append((math.atan2(P[1] - points[i][1], P[0] - points[i][0]), points[i]))
    
    angle.sort(key = lambda x: (x[0], x[1]))
    angle.pop()

    result.append(P)
    result.append(angle[0][1])

    result_idx = 1
    angle_idx = 1

    while angle_idx < count - 1:
        result.append(angle[angle_idx][1])
        result_idx += 1
        
        if ccw(result[result_idx - 2], result[result_idx - 1], result[result_idx]):
            angle_idx += 1
        else:
            while ccw(result[result_idx - 2], result[result_idx - 1], result[result_idx]) == False:
                result.pop(result_idx - 1)
                result_idx -= 1
            
            angle_idx += 1

    if ccw(result[result_idx - 1], result[result_idx], P) == False:
        result.pop()

    print(result)


# if __name__ == "__main__":
#     grahamScan([(0, 0), (-2, -1), (-1, 1), (1, -1), (3, -1), (-3, -1)])
#     grahamScan([(4,2), (3,-1), (2,-2), (1,0), (0,2), (0,-2), (-1,1), (-2,-1), (-2,-3), (-3,3), (-4,0), (-4,-2), (-4,-4)])
