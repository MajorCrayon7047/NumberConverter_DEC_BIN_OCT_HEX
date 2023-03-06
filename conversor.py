from conversorClass import Conversor

c = Conversor()
while True:
    n = input('DEC(d), BIN(b), OCT(o) y HEX(h): ').lower()
    match n:
        case "d":
            resultado = c.dec(int(input('Numero decimal:    ')), int(input('Base a convertir:   ')))
            print(resultado)
        case 'b':
            resultado = c.bin(input('Numero BINARIO: '), input('Base a convertir: '))
            print(resultado)
        case 'o':
            resultado = c.oct(input('Numero OCTAL: '), input('Base a convertir: '))
            print(resultado)
        case 'h':
            resultado = c.hex(input('Numero HEXADECIMAL: ').lower(), input('Base a convertir: '))
            print(resultado)