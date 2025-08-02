import sys

def test(char, index, array):
    count = 1
    for item in range(index - 1, -1, -1):
        if char == array[item]:
            return count
        count += 1
    return -1

def solution(s):
    array = list(s)
    answer = []
    index = 0
    
    for char in array:
        result = test(char, index, array)
        index += 1
        answer.append(result)

    return answer

print(solution("banana"))