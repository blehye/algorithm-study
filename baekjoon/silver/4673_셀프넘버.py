# 10000보다 작은 셀프 넘버 한줄에 하나씩 출력

array = [ i for i in range(1, 10001)]

def calAndRemoveNum(inputNumber):
    if inputNumber > 10000:
        return
    number_sum = 0
    for num in str(inputNumber):
        number_sum += int(num)

    number_sum += int(inputNumber)
    if number_sum in array:
        array.remove(number_sum)
        calAndRemoveNum(number_sum)
    else:
        return

for item in array:
    calAndRemoveNum(item)

for item in array:
    print(item)


