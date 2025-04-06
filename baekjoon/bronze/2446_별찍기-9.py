import sys

input = sys.stdin.readline

N = int(input())

max_start_length = 2 * (N - 1) + 1

star_count = max_start_length
for _ in range(N):
    blank_count = (max_start_length - star_count) // 2
    print(" " * blank_count, end="")
    print("*" * star_count, end="")
    if blank_count != 0:
        print(" ", end="")
    print()
    star_count -= 2
star_count = 3
for _ in range(N - 1):
    blank_count = (max_start_length - star_count) // 2
    print(" " * blank_count, end="")
    print("*" * star_count, end="")
    if blank_count != 0:
        print(" ", end="")
    print()
    star_count += 2