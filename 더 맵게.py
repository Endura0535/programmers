import heapq

def solution(scoville, K):

    # scoville 배열 heapq 로 구성
    heapq.heapify(scoville)
    count = 0

    for i in range(len(scoville)-1):
        food1 = heapq.heappop(scoville)

        if food1 > K-1:
            return count

        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + food2*2)
        count += 1

    if heapq.heappop(scoville) > K - 1:
        return count

    return -1
