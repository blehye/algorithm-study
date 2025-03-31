# BOJ 1049

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

package = []
seperate = []

for i in range(M):
    a, b = map(int, input().split())
    package.append(a)
    seperate.append(b)

package.sort()
seperate.sort()

package_price = package[0]
seperate_price = seperate[0]
package_count = N // 6  
seperate_count = N % 6

def solution(package_price, seperate_price, package_count, seperate_count):
    # 패키지 포함하여 사는게 저렴한 경우
    if package_price < seperate_price * 6:
        if package_price < seperate_price * seperate_count:
            return package_price * (package_count + 1)
        return package_price * package_count + seperate_price * seperate_count
    else: # 낱개로 전부 사는게 저렴한 경우
        return seperate_price * N

print(solution(package_price, seperate_price, package_count, seperate_count))

