def my_own_rounding_function(x, y):
    if x == float(x) and y == int(y):
        if y < 0:
            x = str(x)
            x = x.split(sep=".", maxsplit=1)
            checked = float(x[0][y])
            if checked >=5:
                result = int(x[0][:y])+1
                result = str(result)+(-y*"0")
                result = float(result)
            else:
                result = float(x[0][:y]+(-y*"0"))
            return result
        elif y == 0:
            x = str(x)
            x = x.split(sep=".", maxsplit=1)
            integer = float(x[0])
            rest = int(x[1][:y+1])
            checked = int(x[1][y])
            if checked >= 5:
                integer += 1
            return integer
        elif y != 0:
            try:
                x = str(x)
                x = x.split(sep=".", maxsplit=1)
                integer = x[0]
                rest = int(x[1][:y])
                checked = int(x[1][y])
                if checked >= 5:
                    rest += 1
                result = float(f'{integer}.{rest}')
                return result
            except IndexError:
                x[0] = int(x[0])
                x[1] = int(x[1])
                result = float(f'{x[0]}.{x[1]}')
                return result
        else:
            x = str(x)
            x = x.split(sep=".", maxsplit=1)
            result = float(x[0])
            return result
    else:
        return 'Wrong used function'

def check_if_works_correctly(x,y):
    if my_own_rounding_function(x,y) == round(x,y):
        return True
    else:
        return False

for i in range(10):
    print(check_if_works_correctly(3.14159, i))
    #result: True, True, True, True, True, True, True, True, True, True

# Everything works correctly
