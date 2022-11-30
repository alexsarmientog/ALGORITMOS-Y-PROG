from Cliente import Cliente
class ToolCarpinteria(Cliente):
    def __init__(self, brand, color, precio, pago, tipo, garantia, facturas):
        super().__init__(brand, color, precio, pago, tipo, garantia, facturas)
    def ver(self):
        print(f"\n Marca: {self.brand} \n Color: {self.color} \n Precio: {self.precio} \n Tipo de herramienta: {self.tipo} \n Garantía: {self.garantia} \n")
        for factura in self.facturas:
            print(f"Facturas: {factura.show()}")  