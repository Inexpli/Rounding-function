def zaokraglij(x, y):
    if x == float(x) and y == int(y):
        if y < 0:
            x = str(x)
            x = x.split(sep=".", maxsplit=1)
            sprawdzana = float(x[0][y])
            if sprawdzana >=5:
                wynik = int(x[0][:y])+1
                wynik = str(wynik)+(-y*"0")
                wynik = float(wynik)
            else:
                wynik = float(x[0][:y]+(-y*"0"))
            return wynik
        elif y == 0:
            x = str(x)
            x = x.split(sep=".", maxsplit=1)
            calosc = float(x[0])
            reszta = int(x[1][:y+1])
            sprawdzana = int(x[1][y])
            if sprawdzana >= 5:
                calosc += 1
            return calosc
        elif y != 0:
            try:
                x = str(x)
                x = x.split(sep=".", maxsplit=1)
                calosc = x[0]
                reszta = int(x[1][:y])
                sprawdzana = int(x[1][y])
                if sprawdzana >= 5:
                    reszta += 1
                wynik = float(f'{calosc}.{reszta}')
                return wynik
            except IndexError:
                x[0] = int(x[0])
                x[1] = int(x[1])
                wynik = float(f'{x[0]}.{x[1]}')
                return wynik
        else:
            x = str(x)
            x = x.split(sep=".", maxsplit=1)
            wynik = float(x[0])
            return wynik
    else:
        return 'Wrong used function'
