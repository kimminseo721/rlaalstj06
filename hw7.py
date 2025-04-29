shopping_bag = {}

print('[구입]')
while True:
  item = input('상품명? ')
  if item == '':
    print()
    break
  else:
    amount = int(input('수량은? '))
    print(f'장바구니에 {item} {amount}개가 담겼습니다.')
    shopping_bag[item] = amount
  print()

print(f'>>> 장바구니 보기: {shopping_bag}')

print()

answer = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{answer}은(는) {shopping_bag[answer]}개 담겨 있습니다.')
