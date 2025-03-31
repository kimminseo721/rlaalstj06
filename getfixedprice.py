def get_fixed_price(price, rate):
    result = int(price / ((100 - rate)/100))
    return result
