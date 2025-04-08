# 티셔츠 : 6가지 사이즈, 같은사이즈로 T장 묶음 주문
# 펜 : 1가지 종류, P자루씩 묶음 주문, 한자루씩 주문

import sys
input = sys.stdin.readline

N = int(input())

size_arr = list(map(int, input().split()))


T, P = map(int, input().split())


tshirt_set = 0

for size in size_arr:
    x = size // T
    y = size % T
    if y != 0:
        tshirt_set += x + 1
    else:
        tshirt_set += x

print(tshirt_set)
print(N // P, N % P)
