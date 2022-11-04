class Calculadora:
    def multiplicacion(numero1,numero2):
        try:
            int(numero1)
            int(numero2)
            print(numero1*numero2)
        except ValueError:
            print("ERROR valor no valido")
    def potencia(numero1,numero2):
        try:
            int(numero1)
            int(numero2)
            print(numero1**numero2)
        except ValueError:
             print("ERROR valor no valido")
calculadora = Calculadora()
Calculadora.multiplicacion(2,3)