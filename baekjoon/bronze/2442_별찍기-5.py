import sys
input = sys.stdin.readline

N = int(input())

last_star_count = 2 * (N - 1) + 1

i = 1
for j in range(1, N + 1):
    blank_count = (last_star_count - i ) // 2
    print(" " * blank_count, end="")
    print("*" * i, end="")
    if blank_count != 0:
        print(" ", end="")
    print()
    i += 2