from sys import stdin

input = stdin.readline

n = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            arr[j][k] = 1
          
cnt = 0  
for i in range(100):
    c = arr[i].count(1)
    cnt += c
    
print(cnt)

