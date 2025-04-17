import sys
from collections import deque

input = sys.stdin.readline
status = True

while True:
    inputString = input().rstrip()
    if inputString == ".":
        break
    stack = deque()
    status = True
    for char in inputString:
        if char == "[":
            stack.append(char)
        elif char == "(":
            stack.append(char)
        elif char == "]":
            if len(stack) == 0:
                status = False
                break
            popChar = stack.pop()
            if popChar != "[":
                status = False
                break
        elif char == ")":
            if len(stack) == 0:
                status = False
                break
            popChar = stack .pop()
            if popChar != "(":
                status = False
                break
    if status and len(stack) == 0:
        print("yes")
    else:
        print("no")
