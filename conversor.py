from conversorClass import Conversor

c = Conversor()
while True:
    n = input('En que base esta el numero?\nDEC(d), BIN(b), OCT(o) y HEX(h): ').lower()
    try:
        match n:
            case "d":
                num = input('Numero en decimal:    ')
                b = input('Base a convertir:   ')
                resultado = c.dec(int(num), int(b))
                print(f"Resultado en base ({b}): {resultado}\n\n")
            case 'b':
                num = input('Numero en BINARIO: ')
                b = input('Base a convertir: ')
                resultado = c.bin(num, b)
                print(f"Resultado en base ({b}): {resultado}\n\n")
            case 'o':
                num = input('Numero en OCTAL: ')
                b = input('Base a convertir: ')
                resultado = c.oct(num, b)
                print(f"Resultado en base ({b}): {resultado}\n\n")
            case 'h':
                num = input('Numero en HEXADECIMAL: ').lower()
                b = input('Base a convertir: ')
                resultado = c.hex(num, b)
                print(f"Resultado en base ({b}): {resultado}\n\n")
    except Exception as err:
        #print(err)
        print("Ocurrio un error porfavor ingrese los datos correctamente\n---------------\n\n")