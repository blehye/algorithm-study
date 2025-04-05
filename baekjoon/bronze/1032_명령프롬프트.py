import sys

input = sys.stdin.readline

N = int(input())

text = input().rstrip()
text_len = len(text)
change_index = []

for _ in range(N-1):
    input_text = input().rstrip()
    for i in range(text_len):
        if text[i] == input_text[i]:
            continue
        else:
            change_index.append(i)

index = 0
for char in text:
    if index in change_index:
        print("?", end="")
    else:
        print(char, end="")
    index += 1
    
    