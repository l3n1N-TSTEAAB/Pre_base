##inicio
class Productos():
    def __init__(self,IdProducto,Nombre,IdCategoria,Precio,TotalCompras,TotalVentas,Stock):
        self.IdProducto = IdProducto
        self.Nombre = Nombre
        self.IdCategoria = IdCategoria
        self.Precio = Precio
        self.TotalCompras = TotalCompras
        self.TotalVentas = TotalVentas
        self.Stock = Stock

    def mostrarProductos(self):
        return (f"Codigo: {self.IdProducto} - Nombre: {self.nombre} - Categoria: {self.categoria} Precio: {self.Precio}"
                f"Total Compras: {self.TotalCompras} - Total Ventas: {self.TotalVentas} - Stock: {self.Stock}")


class RegistroProducto():
        def __init__(self):
            self.productos = {}

        def agregar_producto(self):
            while True:
                IdProducto = input("Ingresa el ID del producto: ").strip()
                if not IdProducto:
                    print("ERROR: CODIGO VACIO.\n")
                    continue
                if IdProducto in self.productos:
                    print(f"Error: El código '{IdProducto}' ya está registrado.\n")
                    continue
                break

            while True:
                Nombre = input("Ingrese nombre del producto: ").strip()
                if not Nombre:
                    print("Error: El nombre no puede estar vacío.\n")
                    continue
                break

            categorias = {"ALIMENTOS","HIGIENE","ELECTRODOMESTICOS",""}
            while True:
                try:
                    IdCategoria = input("Ingresa el ID del categoria: ").strip()


                except:












class Categoria():
    def __init__(self,IdCategoria,NombreCa):
        self.IdCategoria = IdCategoria
        self.Nombre = NombreCa

class Clientes():
    def __init__(self,NitCli,NombreCl,Direccion,Telefono,Correo):
        self.NitCli = NitCli
        self.Nombre = NombreCl
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo

class Proveedores():
    def __init__(self,NitProo,NombreProv,DireccionProv,TelefonoProv,CorreoProv,EmpresaProv):
        self.NitProo = NitProo
        self.NombreProv = NombreProv
        self.DireccionProv = DireccionProv
        self.TelefonoProv = TelefonoProv
        self.CorreoProv = CorreoProv
        self.EmpresaProv = EmpresaProv

class Empleados():
    def __init__(self,IdEmpleado,NombreEmp,DireccionEmp,TelefonoEmp,CorreoEmp,PuestaEmp):
        self.IdEmpleado = IdEmpleado
        self.NombreEmp = NombreEmp
        self.DireccionEmp = DireccionEmp
        self.TelefonoEmp = TelefonoEmp
        self.CorreoEmp = CorreoEmp
        self.PuestaEmp = PuestaEmp

class Ventas():
    def __init__(self,IdVenta,FechaVenta,IdEmpleado,NitCli,TotalVenta):
        self.IdVenta = IdVenta
        self.FechaVenta = FechaVenta
        self.IdEmpleado = IdEmpleado
        self.NitCli = NitCli
        self.TotalVenta = TotalVenta

class DetalleVentas():
    def __init__(self,IdDetalleVenta,IdVenta,CantidadVenta,IdProducto,Subtotal,Stock):
        self.IdDetalleVenta = IdDetalleVenta
        self.IdVenta = IdVenta
        self.CantidadVenta = CantidadVenta
        self.IdProducto = IdProducto
        self.Subtotal = Subtotal
        self.Stock = Stock

class Compras():
    def __init__(self,IdCompra,FechaIngreso,IdEmpleado,NitProo,Total):
        self.IdCompra = IdCompra
        self.FechaIngreso = FechaIngreso
        self.IdEmpleado = IdEmpleado
        self.NitProo = NitProo
        self.Total = Total

class DetalleCompras():
    def __init__(self,IdDetalleCompra,IdVenta,CantidadCompra,IdProducto,Subtotal,FechaCad):
        self.IdDetalleCompra = IdDetalleCompra
        self.IdVenta = IdVenta
        self.CantidadCompra = CantidadCompra
        self.IdProducto = IdProducto
        self.Subtotal = Subtotal
        self.FechaCad = FechaCad
