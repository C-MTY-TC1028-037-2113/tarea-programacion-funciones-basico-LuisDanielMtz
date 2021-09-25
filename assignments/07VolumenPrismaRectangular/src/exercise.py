# Escribe aquí tus funciones...
def area(base,altura):
    #resolver problema 
    return base*altura

def volumen_prisma(base,altura,profundidad):
      return  area (base, profundidad)*altura 
                             

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = volumen_prisma(b,a,p)

    print("El volumen del prisma es:",r)

if __name__=='__main__':
    main()
