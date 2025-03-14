def get_radius(prompt):
    r = int(input(prompt))
    return r

def circle_area(rad):
    print('반지름이', rad, '인 원의 넓이 = ', '3.14 x', rad, 'x', rad, '=')
    return rad*rad*3.14

input_value = get_radius('넓이를 구하고자 하는 원의 반지름은?:')
result = circle_area(input_value)
print(result)
