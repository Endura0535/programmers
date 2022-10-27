from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        n = prices.popleft()
        sec = 0
        for p in prices:
            sec += 1
            if n > p:
                break
        answer.append(sec)

    return answer