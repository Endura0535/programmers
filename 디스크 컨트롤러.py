'''
type: heap
'''

import heapq

def solution(jobs):
    time, now, i, start = 0, 0, 0, -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if heap == []:
            now += 1
        else:
            job = heapq.heappop(heap)
            start = now
            now += job[0]
            time += now - job[1]
            i += 1

    answer = time//len(jobs)

    return answer


print(solution([[24, 10], [28, 39], [43, 20], [35, 45], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
print(solution([[0, 6], [2, 8], [3, 7], [7, 1], [11, 11], [19, 25], [30, 15], [32, 6], [40, 3]]))