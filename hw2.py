def get_integer(prompt):
    change_cash = int(input(prompt))
    return change_cash

def exchange(cash):
    a = cash // 500
    A = cash % 500
    
    b = A // 100
    B = A % 100
    
    c = B // 50
    C = B % 50

    d = C // 10
    D = C % 10
    print('500원 동전의 개수:', a)
    print('100원 동전의 개수:', b)
    print('50원 동전의 개수:', c)
    print('10원 동전의 개수:', d)

input_value = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(input_value)
