from Cliente import Cliente
from Tool_carpintería import ToolCarpinteria
from Tool_herreria import ToolHerreria
from Tool_plomeria import ToolPlomeria
from Factura import Factura

class App():
    def __init__(self):
        self.cliente = []
    
    def registrar_cliente(self):
        print("\n Para registrar un cliente es necesario que llene la informacion pedida a continuacion \n")
        nombre = input("Ingrese el nombre del clinete: ")
        apellido = input("Ingrese el apellido del cliente: ")
        edad = int(input("Ingrese la edad del cliente: "))
        cedula = int(input("Ingrese la cedula del cliente (sin puntos ni letras): "))
        telefono = int(input("Ingrese el numero de telefono del cliente (sin espacios): "))
        while not cedula.isnumeric():
            cedula = input("Ingreso invalido. Ingrese la cedula del cliente (sin puntos ni letras): ")
        while not numero.isnumeric():
            numero = input("Ingreso invalido. Ingrese el numero de telefono del cliente (sin puntos ni letras): ")
        facturas = ""

    def estadisticas(self):
        """1"""
        pagos = 0
        for cliente in self.cliente:
            for factura in cliente.facturas:
                pagos += factura.pago 
        print(f"\n El monto total pagado por el cliente es: {pagos}")
        '''2'''
        herreria = 0
        carpinteria = 0
        plomeria = 0
        for herramientas in self.herramientas:
            if herramientas.tipo == "herreria":
                herreria += 1
            if herramientas.tipo == "carpinteria":
                carpinteria += 1
            if herramientas.tipo == "plomeria":
                plomeria += 1
        print(f"\n El total de herramientas compradas por tipo es: \n Herreria: {herreria} \n Carpinteria: {carpinteria} \n Plomeria: {plomeria}")
            
    def start(self):
        print("\n Bienvenido a Saman Tools!")
        while True:
            menu = input("\n 1. Registrar cliente \n 2. Estadisticas: ")
            while not menu.isnumeric() and menu not in range(1, 5):
                menu = input("Ingreso invalido. Intente de nuevo: ")
            if menu == "1":
                self.registrar()
            if menu == "2":
                self.estadisticas()
                break