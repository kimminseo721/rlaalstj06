def display_multiplication_table():
    i = 1
    j = 2
    while i <= 9:
        while j < 6:
            print(f'{j} x {i} = {j*i:2d}', end='\t')
            j += 1
        i += 1
        j = 2
        print()
    
    print()

    i = 1
    j = 6
    while i <= 9:
        while j < 10:
            print(f'{j} x {i} = {j*i:2d}', end='\t')
            j += 1
        i += 1
        j = 6
        print()

display_multiplication_table()
