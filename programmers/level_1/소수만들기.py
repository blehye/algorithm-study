from itertools import combinations

def check_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for item in combi:
        if check_prime_number(sum(item)):
            answer += 1
    return answer

x = solution([1,2,3,4])
print(x) # 1

x = solution([1,2,7,6,4])
print(x) # 4

