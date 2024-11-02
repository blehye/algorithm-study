import sys

# N명의 모험가가 있고 각각 공포도가 있음
# 공포도가 X인 모험가는 반드시 X명 이상의 모험가 그룹에 참여해야함
# 최대 모험가 그룹 수 구하기


def solution(horror_list):
    group_count = 0
    adventurer_count = 0
    for horror in horror_list:
        adventurer_count += 1
        if adventurer_count >= horror:
            group_count += 1
            adventurer_count = 0
    return group_count


input = sys.stdin.readline

# 모험가의 수
N = input().rstrip()
# 공포도 배열
horror_list = list(map(int, input().rstrip().split(" ")))

horror_list = sorted(horror_list)

horror_len = len(horror_list)

print(solution(horror_list))
