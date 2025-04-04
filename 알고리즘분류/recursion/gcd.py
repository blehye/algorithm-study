# 유클리드 호제법을 이용한 최대공약수 계산
# A, B(A > B) 가 있을때 A와 B의 최대공약수는 B와 A를 B로 나눈 나머지의 최대공약수와 같다


A = int(input())
B = int(input())


def gcd(A, B):
    if A % B == 0:
        return B
    return gcd(B, A % B)


print(gcd(A, B))
