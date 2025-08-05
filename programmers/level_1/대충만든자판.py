def solution(keymap, targets):

    char_dict = dict()
    result_list = []

    for key_info in keymap:
        char_list = list(key_info)
        index = 1
        for char in char_list:
            if char not in char_dict:
                char_dict[char] = index
            else:
                origin_value = char_dict[char]
                if index < origin_value:
                    char_dict[char] = index
            index += 1
    
    for target in targets:
        sum = 0
        for char in target:
            if char in char_dict:
                char_index = char_dict[char]
                sum += char_index
            else:
                sum = -1
                break
        result_list.append(sum)
    return result_list

x = solution(["ABACD", "BCEFD"],["ABCD","AABB"])
# [9, 4]
print(x)
x = solution(["AA"],["B"])
# [-1] 
print(x)
x = solution(["AGZ", "BSSS"],["ASA","BGZ"])
# [4, 6]
print(x)
