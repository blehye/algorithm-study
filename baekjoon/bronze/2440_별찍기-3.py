import sys
input = sys.stdin.readline

N = int(input())
M = N

for i in range(N):
    for j in range(M):
        print("*", end="")
    print()
    M -= 1