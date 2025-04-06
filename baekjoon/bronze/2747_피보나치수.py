import sys
sys.setrecursionlimit(3000)

input = sys.stdin.readline

N = int(input())

target_index = N

index = 2

def getFibonacci(beforeNum1, beforeNum2):
    global index

    index += 1
    afterNum = beforeNum1 + beforeNum2

    if index == target_index:
        print(afterNum)
        return

    getFibonacci(beforeNum2, afterNum)

if target_index == 1 or target_index == 2:
    print(1)
else:
    getFibonacci(1, 1)