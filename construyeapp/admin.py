from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Agencia
from .models import Carrito
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio","description", "unidades")
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible","precio")
    delete_confirmation_template: str



admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Agencia)
admin.site.register(Carrito)