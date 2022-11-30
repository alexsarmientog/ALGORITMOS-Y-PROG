class Comprobante():
    def __init__(self, nombre, apellido, cedula, estado_civil, cuenta, tipo_operacion, monto, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.estado_civil = estado_civil
        self.cuenta = cuenta
        self.tipo_operacion = tipo_operacion
        self.monto = monto
        self.saldo = saldo
    def show(self):
        print(f"Factura: Cliente: {self.nombre} {self.apellido} \n Cedula: {self.cedula} \n Estado civil: {self.estado_civil} \n Tipo de operacion: {self.tipo_operacion} \n Monto de la operación: {self.monto} \n Saldo final: {self.saldo}") 