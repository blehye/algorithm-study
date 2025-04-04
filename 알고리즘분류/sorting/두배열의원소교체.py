# 두 개의 배열 A, B, N개의 원소로 구성됨
# 최대 K번의 바꿔치기 연산 수행가능
# 배열 A의 모든 원소의 합이 최대가 되도록 하는것이 목표
# 배열 A의 모든 원소의 합의 최댓값 출력


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))
