from django.db import models

# Modelo para representar las categorías de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categorias'  # Nombre explícito para la tabla en la base de datos


# Modelo para los servicios que ofrece la empresa
class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Guarda la imagen como binario
    imagen = models.BinaryField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicios'


# Modelo para productos en inventario
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.BinaryField()

    # Relación con categoría (cuando se elimina una categoría, sus productos también se eliminan)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'


# Modelo de ventas de servicios
class VentaServicio(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_completo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    detalles = models.TextField()
    fecha_venta = models.DateField()

    # Relación con el servicio vendido
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta de {self.servicio.nombre} por {self.nombre_completo}"

    class Meta:
        db_table = 'venta_servicios'
        ordering = ['-fecha_venta']  # Ordenar por fecha de venta descendente


# Modelo para mensajes enviados desde formulario de contacto
class Mensaje(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha se genera automáticamente al guardar

    def __str__(self):
        return f"Mensaje de {self.nombre}"

    class Meta:
        db_table = 'mensajes'
        ordering = ['-fecha']  # Ordenar mensajes más recientes primero
