# 정수 N이 입력되면 00시00분00초부터 N시 59분 59초까지 모든 시각중에서
# 3이 하나라도 포함되는 모든 경우의 수 구하기

import sys

input = sys.stdin.readline

N = int(input().rstrip())

count = 0

for i in range(0, N + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)
