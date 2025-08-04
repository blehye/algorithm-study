def solution(s):
    char_list = list(s)
    word_list = []
    first_char = char_list[0]
    index = 0
    first_index = 0

    # 같은 글자 카운트
    same_char_count = 0
    # 다른 글자 카운트
    diff_char_count = 0

    for char in char_list:
        if char == first_char:
            same_char_count += 1
        else:
            diff_char_count += 1

        index += 1
        if same_char_count == diff_char_count:
            word_list.append(s[first_index:index])

            if index == len(s):
                break

            first_index = index
            first_char = char_list[first_index]
            same_char_count = 0
            diff_char_count = 0
        if index == len(s):
            word_list.append("1")
    return len(word_list)

x = solution('banana')
print(x)
x = solution('abracadabra')
print(x)
x = solution('aaabbaccccabba')
print(x)