# 절단기에 높이H를 지정하면 떡을 한번에 절단
# 높이가 19, 14, 10, 17 인 떡이 있고 절단기 높이를 15로 설정한다면
# 15, 14, 10, 15가 될것
# 잘린 떡의 길이는 4, 0, 0, 2 손님은 6만큼의 길이를 가져간다
# 손님이 왔을때 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기위해 절단기 높이 최댓값 구하기

# N: 떡의개수 M: 요청한 떡의 길이
N, M = map(int, input().split())

# 떡의 개별 높이
array = list(map(int, input().split()))
total_length = sum(array)
start = 0
end = max(array)


def binary_search():
    global start
    global end
    while start <= end:
        mid = (start + end) // 2

        length = calculate_length(mid)

        if M == length:
            return mid
        elif M < length:
            start = mid + 1
        else:
            end = mid - 1


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
