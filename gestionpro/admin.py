from django.contrib import admin
from .models import Categoria, Producto, Servicio, VentaServicio, Mensaje
from .forms import ServicioForm, ProductoForm

class ServicioAdmin(admin.ModelAdmin):
    form = ServicioForm

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm


admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(VentaServicio)
admin.site.register(Mensaje)