# ===> Palindromos

while True:
    string = input()
    if string != 'fim':
        def testePalindromo(texto):
            textoLimpo = texto.replace(' ', '')
            stringLower = textoLimpo.lower()
            stringInvetida = stringLower[::-1]
            if stringInvetida == stringLower:
                return 'é palindromo'
            else:
                return 'não é palindromo'
        print(testePalindromo(string))
    else:
        exit()



