# k : 사과의 최대 점수
# m : 한 상자에 들어가는 사과의 수
# score : 사과들의 점수

def solution(k, m, score):
    # 점수 내림차순으로 정렬
    score_list = sorted(score, reverse=True)

    count = 0

    price_list = []
    for s in score_list:
        count += 1
        if count == m:
            price = s * m
            price_list.append(price)
            count = 0
    return sum(price_list)

x = solution(3, 4, [1,2,3,1,2,3,1])
y = solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
print(x)
print(y)