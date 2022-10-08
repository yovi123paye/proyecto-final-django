from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"carritos", views.CarritoViewSet)
router.register(r"agencias", views.AgenciaViewSet)

#direcciones URL
urlpatterns = [     
    path('', include(router.urls)),
    path('productos/', views.ProductoListarViewSet.as_view(), name='Gestion de Productos'),
    path('carritos/<str:agenciaId>', views.carritos_compras, name='agenciaId'),
]