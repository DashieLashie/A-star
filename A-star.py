import numpy as num
import queue


def countHeuristic(heu, final, current):
    for i in range(size):
        for j in range(size):
            if (current[i][j] != final[i][j]):
                heu += 1
            if (current[i][j] == -1 & final[i][j] == -1):
                heu += 1
    heu -= 1
    return heu

def defineNeighbors(size, x, y):
    Hood = num.array([[x-1,y],[x+1,y],[x, y-1],[x, y+1]])
    noHood = num.where((Hood == -1) | (Hood == size))

    if len(notHood[0]) == 2:
        Hood = num.delete(Hood, noHood[0][0], 0)
        Hood = num.delete(Hood, noHood[0][1]-1, 0)
    elif len(noHood[0]) == 1:
        Hood = num.delete(Hood, noHood[0][0], 0)

    return Hood




size = 3

start = num.array([
    [2,8,3],
    [1,-1,4],
    [7,6,5]
])
final = num.array([
    [1,2,3],
    [8,-1,4],
    [7,6,5]
])

temp = num.empty_like(start)
temp[:] = start
run = num.empty_like(start)
run[:] = temp
parent = num.empty_like(start)
parent[:] = run

Pq = queue.PriorityQueue()
support = num.array([])

