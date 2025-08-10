def solution(n, w, num):
    total_list = []
    for i in range(w):
        total_list.append([])

    target_num = 1
    reverse_count = 0
    is_reversed = False
    num_index = 1
    while target_num <= n:
        index = target_num % w  
        if not is_reversed:
            total_list[index-1].append(target_num)
            if target_num == num:
                num_index = index - 1
        else:
            index_result = w - index
            if index == 0:
                index_result = 0
            total_list[index_result].append(target_num)
            if target_num == num:
                num_index = index_result

        target_num += 1
        reverse_count += 1

        if reverse_count == w:
            is_reversed = not is_reversed
            reverse_count = 0
    
    num_index_result = total_list[num_index].index(num)

    return len(total_list[num_index]) - num_index_result

x = solution(22, 6, 8)
print(x) # 3

x = solution(13, 3, 6)
print(x) # 4

