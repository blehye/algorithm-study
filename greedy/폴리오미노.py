# BOJ 1343

import sys

input = sys.stdin.readline

array = input().strip().split('.')

result = "";
A_FLAG = "AAAA"
B_FLAG = "BB"
flag = True

for i in range(len(array)):
    target = array[i]
    if len(target) % 2 == 1:
        print(-1)
        flag = False
        break
    elif target == '':
        result += '.'
        continue
    else:
        aCount = len(target) // 4
        bCount = (len(target) % 4) // 2
        result += A_FLAG * aCount + B_FLAG * bCount
        result += '.'
if flag:
    print(result[:-1])