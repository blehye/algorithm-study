import sys
input = sys.stdin.readline

input_str = input().rstrip()

input_str_len = len(input_str)
start = 0
end = 10

while True:
    if end >= input_str_len:
        end = input_str_len
    if start > input_str_len - 1:
        break
    print(input_str[start:end])
    start += 10
    end += 10