import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    array = dict()
    N = int(input())
    note1 = list(map(int, input().split()))

    M = int(input())
    note2 = list(map(int, input().split()))

    for item in note1:
        array[item] = True

    for item in note2:
        if item in array:
            print(1)
        else:
            print(0)