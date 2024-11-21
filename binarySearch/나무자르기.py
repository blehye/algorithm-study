N, M = map(int, input().split())

array = list(map(int, input().split()))
total_length = sum(array)
start = 0
end = max(array)
mid = (start + end) // 2
before_mid = mid


def binary_search():
    global start
    global end
    global mid
    global before_mid

    while start <= end:
        mid = (start + end) // 2

        length = calculate_length(mid)

        if M == length:
            return mid
        elif M < length:
            start = mid + 1
            before_mid = mid
        else:
            end = mid - 1
        if start > end and M >= length:
            return before_mid
    return before_mid


def calculate_length(height):
    global total_length
    result = 0
    for item in array:
        length = item - height
        if length > 0:
            result += length
    total_length = result
    return result


print(binary_search())
