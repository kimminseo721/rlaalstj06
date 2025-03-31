def get_fixed_price(price, rate):
    result = int(price / ((100 - rate)/100))
    return result

def main():
    r = int(input('할인율은? '))
    p1 = int(input('A 상품의 할인된 가격은? '))
    p2 = int(input('B 상품의 할인된 가격은? '))
    A = get_fixed_price(p1, r)
    B = get_fixed_price(p2, r)
    print('A상품의 정가는', A, '원')
    print('B상품의 정가는', B, '원')

if __name__ == '__main__':
    main()
