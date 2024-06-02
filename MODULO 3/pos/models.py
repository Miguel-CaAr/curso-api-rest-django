from django.db import models
from cloudinary.models import CloudinaryField


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = CloudinaryField('image', default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT,
                                  related_name='Productos',)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    codigo = models.CharField(max_length=10)
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, related_name="PedidoProductos",
                               on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
