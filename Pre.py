##inicio


class Productos():
    def __init__(self,IdProducto,Nombre,Precio,IdCategoria,TotalCompras,TotalVentas,Stock):
        self.Nombre = Nombre
        self.Precio = Precio
        self.IdCategoria = IdCategoria
        self.TotalCompras = TotalCompras
        self.TotalVentas = TotalVentas
        self.Stock = Stock


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


