# ===> Conversão de número decimal para bases de 2 a 9

while True:
    num = int(input())

    if (num != 1) and (num <= 100) and (num >= 0):
        for base in range(2, 10):
            def converte(numDecimal, base):
                resto = numDecimal % base
                if numDecimal <= 1:
                    numConvertido = int(str(numDecimal))
                else:
                    numConvertido = int(str(converte(numDecimal // base, base)) + str(resto))

                return numConvertido


            print(converte(num, base), end=' ')
    else:
        exit(0)
