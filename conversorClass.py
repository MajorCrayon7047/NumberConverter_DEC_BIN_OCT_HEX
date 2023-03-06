class Conversor:
    def dec(self, num:int, base:int):   #Funcion recursiva para convertir DEC a una base especifica hasta (16)
        cadena = '0123456789ABCDEF'
        
        if num < base:
            return cadena[num]
        else:
            return self.dec(num//base, base) + cadena[num%base]

    def bin(self, num:str, base = 10):   #Convierte BIN a DEC y si hay una base especifica lo pasa a esa base
        result = 0
        pos = len(num)-1
        for n in num:
            result += int(n)*(2**pos)
            pos-=1
        if base != '10':
            result = self.dec(result, int(base))
        return result

    def oct(self, num:str, base = 10):  #Convierte OCT a DEC y si hay una base especifica lo pasa a esa base
        result = 0
        pos = len(num)-1
        for n in num:
            result += int(n)*(8**pos)
            pos-=1
        if base != '10':
            result = self.dec(result, int(base))
        return result

    def hex(self, num:str, base = 10):  #Convierte HEX a DEC y si hay una base especifica lo pasa a esa base
        result = 0
        pos = len(num)-1
        for n in num:
            equivalencias = {"f": 15, "e": 14, "d": 13, "c": 12, "b": 11, "a": 10}
            if n in equivalencias: n = equivalencias[n]
            result += int(n)*(16**pos)
            pos-=1
        if base != '10':
            result = self.dec(result, int(base))
        return result