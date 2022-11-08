def solution(n, times):

    left, right = 1, max(times)*n

    while left <= right:
        mid = (left + right) // 2
        complete = 0
        for t in times:
            complete += mid//t
            if complete >= n:
                break

        if complete >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

print(solution(6,[7,10]))