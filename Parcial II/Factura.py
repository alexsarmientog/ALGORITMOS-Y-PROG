class Factura():
    def __init__(self, nombre, apellido, cedula, telefono, herramienta, cantidad, pago, descuento):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.herramienta = herramienta
        self.cantidad = cantidad 
        self.pago = pago
        self.descuento = descuento
    def show(self):
        print(f"Factura: Cliente: {self.nombre} {self.apellido} \n Cedula: {self.cedula} \n Telefono: {self.cedula} \n Herramienta: {self.herramienta} \n Cuantas compro: {self.cantidad} \n Pago: {self.pago}") 
