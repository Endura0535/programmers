'''
type: heap
'''

def solution(operations):
    answer = []
    queue = []
    for o in operations:
        if o == "D 1":
            if len(queue) == 0:
                continue
            queue.pop(-1)
        elif o == "D -1":
            if len(queue) == 0:
                continue
            queue.pop(0)
        else:
            queue.append(int(o[2:]))
        queue.sort()

    if len(queue) == 0:
        return [0,0]
    elif len(queue) == 1:
        return [queue[0], queue[0]]
    else:
        return [queue[-1], queue[0]]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))