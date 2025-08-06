able_word_list = ["aya", "ye", "woo", "ma"]
able_word_list_without_aya = ["ye", "woo", "ma"]
able_word_list_without_ye = ["aya", "woo", "ma"]
able_word_list_without_woo = ["aya", "ye", "ma"]
able_word_list_without_ma = ["aya", "ye", "woo"]

def check_start_able_word_list(target_word):
    for word in able_word_list:
        if target_word.startswith(word):
            return True, word
    return False, ""

def check_start_without_aya(target_word):
    for word in able_word_list_without_aya:
        if target_word.startswith(word):
            return True, word
    return False, ""

def check_start_without_ye(target_word):
    for word in able_word_list_without_ye:
        if target_word.startswith(word):
            return True, word
    return False, ""

def check_start_without_woo(target_word):
    for word in able_word_list_without_woo:
        if target_word.startswith(word):
            return True, word
    return False, ""

def check_start_without_ma(target_word):
    for word in able_word_list_without_ma:
        if target_word.startswith(word):
            return True, word
    return False, ""

def solution(babbling):
    answer = 0

    for word in babbling:
        target_word = word

        result, result_word = check_start_able_word_list(target_word)
        if not result:
            continue

        target_word = target_word[len(result_word):]

        while True:
            if target_word == '':
                answer += 1
                break

            if result_word == 'aya':
                result, result_word = check_start_without_aya(target_word)
                if not result:
                    break
                target_word = target_word[len(result_word):]
            elif result_word == 'ye':
                result, result_word = check_start_without_ye(target_word)
                if not result:
                    break
                target_word = target_word[len(result_word):]
            elif result_word == 'woo':
                result, result_word = check_start_without_woo(target_word)
                if not result:
                    break
                target_word = target_word[len(result_word):]
            else:
                result, result_word = check_start_without_ma(target_word)
                if not result:
                    break
                target_word = target_word[len(result_word):]
                    
    return answer

x = solution(["aya", "yee", "u", "maa"])
print(x) # 1
x = solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
print(x) # 2
