def read_single_digit(digit):
    if digit == 0:
        return '영'
    elif digit == 1:
        return '일'
    elif digit == 2:
        return '이'
    elif digit == 3:
        return '삼'
    elif digit == 4:
        return '사'
    elif digit == 5:
        return '오'
    elif digit == 6:
        return '육'
    elif digit == 7:
        return '칠'
    elif digit == 8:
        return '팔'
    elif digit == 9:
        return '구'
    else:
        return ''

def read_number(number):
    if 100 <= number <= 999:
        return read_single_digit(number // 100) + ' ' + read_single_digit((number % 100) // 10) + ' ' + read_single_digit(number % 10)
    else:
        return False



input_value = int(input('세 자리 정수 입력: '))
result = read_number(input_value)
if result == False:
    print('다른 수를 입력해주세요')
else:
    print(result)
