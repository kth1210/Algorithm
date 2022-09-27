import sys

def collinearPoints(points):
    slope = []
    result = []
    resultSlope = []
    points.sort(key = lambda x : (x[0], x[1]))

    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            yc = points[j][1] - points[i][1]
            xc = points[j][0] - points[i][0]

            if xc == 0:
                si = float('inf')
            else:
                si = yc / xc
            slope.append((si, j))
        
        slope.sort()
        SL = len(slope)
        cnt = 1
        temp = slope[0][0]
        for idx in range(1, SL):
            if temp == slope[idx][0]:
                cnt += 1
            else:
                if cnt >= 3 and slope[idx-1] not in resultSlope:
                    result.append((points[i][0], points[i][1], points[slope[idx-1][1]][0], points[slope[idx-1][1]][1]))
                    resultSlope.append(slope[idx-1])
                    temp = slope[idx][0]
                    cnt = 1
                else:
                    temp = slope[idx][0]
                    cnt = 1
        if cnt >= 3 and slope[SL-1] not in resultSlope:
            result.append((points[i][0], points[i][1], points[slope[SL-1][1]][0], points[slope[SL-1][1]][1]))
            resultSlope.append(slope[SL-1])
        slope.clear()
        
    return result

# points = [(19000,10000), (18000,10000), (32000,10000), (21000,10000), (1234,5678), (14000,10000)]
# points = [(10000,0), (0,10000), (3000,7000), (7000,3000), (20000,21000), (3000,4000), (14000,15000), (6000,7000)]
# points = [(0,0), (1,1), (3,3), (4,4), (6,6), (7,7), (9,9)]
# points = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (8,0)]
# points = [(7,0), (14,0), (22,0), (27,0), (31,0), (42,0)]
# points = [(12446,18993), (12798,19345), (12834,19381), (12870,19417), (12906,19453), (12942,19489)]
# points = [(1,1), (2,2), (3,3), (4,4), (2,0), (3,-1), (4,-2), (0,1), (-1,1), (-2,1), (-3,1), (2,1), (3,1), (4,1), (5,1)]
# print(collinearPoints(points))