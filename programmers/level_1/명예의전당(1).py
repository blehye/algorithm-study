def solution(k, score):
    answer = []
    score_list = []

    for s in score:
        score_list.append(s)
        score_list.sort(reverse=True)
        if len(score_list) > k-1:
            answer.append(score_list[k-1])
        else:
            answer.append(score_list[-1])

    return answer

x = solution(3, [10, 100, 20, 150, 1, 100, 200])
print(x) # [10, 10, 10, 20, 20, 100, 100]

x = solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
print(x) # [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]



