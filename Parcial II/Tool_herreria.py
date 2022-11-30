from Cliente import Cliente
class ToolHerreria(Cliente):
    def __init__(self, brand, color, precio, pago, tipo, calor, facturas):
        super().__init__(brand, color, precio, pago, tipo, calor, facturas)
    def ver(self):
        print(f"\n Marca: {self.brand} \n Color: {self.color} \n Precio: {self.precio} \n Tipo de herramienta: {self.tipo} \n Cuanto calor soporta: {self.calor}°C \n")
        for factura in self.facturas:
            print(f"Facturas: {factura.show()}")  
