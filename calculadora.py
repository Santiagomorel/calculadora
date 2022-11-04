class Calculadora:
    def suma(self, numero1, numero2):
        try:
            int(numero1)
            int(numero2)
            print(numero1 + numero2)
        except ValueError:
            print("No se puede realizar la suma porque no se pasaron numeros como valor")
    
    def resta(self, numero1, numero2):
        try:
            int(numero1)
            int(numero2)
            print(numero1 - numero2)
        except ValueError:
            print("No se puede realizar la resta porque no se pasaron numeros como valor")
    
    def raizCuadrada(self, numero):
        try:
            int(numero)
            print(numero ** (1/2))
        except ValueError:
            print("No se puede realizar la raiz porque no se paso un numero como valor")


calculadora = Calculadora()
calculadora.suma(1,2)
calculadora.resta(3,4)