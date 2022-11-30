class Cliente():
    def __init__(self, nombre, apellido, cedula, telefono, descuento, facturas):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.descuento = descuento
        self.facturas = []
        
    def rec_fac(self, n):
        if n == 1:
            return 1
        else:
             return n*self.rec_fac(n-1)
        
    