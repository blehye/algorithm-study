import sys

# 각 자리가 숫자로만 이루어진 문자열 S가 주어졌을 때 숫자 사이에 곱하기 혹은 더하기 연산자를 넣어 만들어질 수 있는 가장 큰 수 구하기
# 모든 연산은 왼쪽에서부터 순서대로 이루어진다


def isSLengthOne():
    if len(number_list) <= 1:
        return number_list[0]


def calculation(target_number, calc_number):
    if target_number <= 1 or calc_number <= 1:
        return target_number + calc_number
    return target_number * calc_number


def solution(number_list):
    target_number = number_list[0]

    for i in range(1, len(number_list)):
        calc_number = number_list[i]
        target_number = calculation(target_number, calc_number)

    return target_number


S = sys.stdin.readline().rstrip()

number_list = list(map(int, list(S)))
print(solution(number_list))
