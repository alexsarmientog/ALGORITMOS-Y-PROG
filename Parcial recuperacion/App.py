from Cliente import Cliente
from Comprobante import Comprobante

class App():
    def __init__(self):
        self.cliente = []
    
    def registrar(self):
        print("\n Para registrar un cliente es necesario que llene la informacion pedida a continuacion \n")
        nombre = input("Ingrese el nombre del trabajador: ")
        apellido = input("Ingrese el apellido del trabajador: ")
        cedula = input("Ingrese la cedula del trabajador (sin puntos ni letras): ")
        while not cedula.isnumeric():
            cedula = input("Ingreso invalido. Ingrese la cedula del trabajador (sin puntos ni letras): ")
        estado_civil = input("ingrese el estado civil del cliente (C para casado, S para soltero y D para divorciado): ")
        if estado_civil == "C":
                estado_civil = "Casado"
        if estado_civil == "S":
                estado_civil = "Soltero"
        if estado_civil == "D":
                estado_civil = "Divorciado"
        cuenta = input("Ingrese que tipo de cuenta desea aperturar (·A· para indicar cuenta de ahorros, ·C· para indicar cuenta corriente): ")
        if cuenta == "C":
                cuenta = "Corriente"
        if cuenta == "A":
                cuenta = "Ahorros"
        comprobante = ""
        print(f"\n Cliente {nombre} registrado exitosamente!")

        def depositar(self):
            accion_requerida = input("Ingrese su numero de cedula: ")
            if accion_requerida == cedula:
                print("Puede continuar con la operacion! ")
            saldo = int(input("Ingrese el monto que quiere depositar: "))
            print("Su deposito ha sido exitoso")
            print(f"\n Su saldo disponible es de {saldo}")
            def retirar(self):
                accion_requerida = input("Ingrese su numero de cedula: ")
                if accion_requerida == cedula:
                    print("Puede continuar con la operacion! ")
                retiro = int(input("Ingrese el monto que quiere retirar: "))
                print("Su retiro ha sido exitoso")
                print(f"\n Su saldo disponible es de {saldo - retiro}")
            def consultar(self):
                accion_requerida = input("Ingrese su numero de cedula: ")
                if accion_requerida == cedula:
                    print("Puede continuar con la operacion! ")
                print(f"\n Su saldo disponible es:{saldo}")
        
        def start(self):
            print("\n Bienvenido a Saman Banks!")
        while True:
            menu = input("\n 1. Registrar cliente \n 2. Realizar un deposito \n 3. Realizar un retiro \n 4. Consultar saldo \n 5. Salir \n Ingrese el numero de la accion que desea realizar: ")
            while not menu.isnumeric() and menu not in range(1, 5):
                menu = input("Ingreso invalido. Intente de nuevo: ")
            if menu == "1":
                self.registrar()
            if menu == "2":
                self.depositar()
            if menu == "3":
                self.retirar()
            if menu == "4":
                self.consultar()
            if menu == "5":
                break
        
        
            
