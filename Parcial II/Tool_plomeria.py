from Cliente import Cliente
class ToolPlomeria(Cliente):
    def __init__(self, brand, color, precio, pago, tipo, pulgadas, facturas):
        super().__init__(brand, color, precio, pago, tipo, pulgadas, facturas)
    def ver(self):
        print(f"\n Marca: {self.brand} \n Color: {self.color} \n Precio: {self.precio} \n Tipo de herramienta: {self.tipo} \n Pulgadas: {self.pulgadas} \n")
        for factura in self.facturas:
            print(f"Facturas: {factura.show()}")  