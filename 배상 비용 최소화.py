import heapq

def solution(no, works):
    result = 0
    works.sort(reverse = True)
    while no > 0:
        if works[0] == 0:
            break
        else:
            heapq._heapreplace_max(works, works[0]-1)
            no -= 1
    
    for work in works:
        result += work ** 2
    
    return result
