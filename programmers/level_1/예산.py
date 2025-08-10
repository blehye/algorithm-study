def solution(d, budget):
    answer = 0

    d.sort()
    for item in d:
        budget -= item
        if budget < 0:
            break
        answer += 1
    return answer

x = solution([1,3,2,5,4], 9)
print(x) # 3

x = solution([2,2,3,3], 10)
print(x) # 4
