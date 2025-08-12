# data = [코드 번호(code), 제조일(date), 최대 수량(maximum), 현재 수량(remain)] 
# data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬

def solution(data, ext, val_ext, sort_by):
    new_data = []

    index = 0
    sort_index = 0
    if ext == "code":
        index = 0
    elif ext == "date":
        index = 1
    elif ext == "maximum":
        index = 2
    else:
        index = 3

    if sort_by == "code":
        sort_index = 0
    elif sort_by == "date":
        sort_index = 1
    elif sort_by == "maximum":
        sort_index = 2
    else:
        sort_index = 3
    
    for arr in data:
        if arr[index] < val_ext:
            new_data.append(arr)
    
    return sorted(new_data, key=lambda x: x[sort_index])

x = solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")
print(x) # [[3,20300401,10,8],[1,20300104,100,80]]


