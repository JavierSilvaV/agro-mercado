from django.urls import path

from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.product_all, name="store_home"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
    path("listar-productos/", views.listar_productos, name="listar-productos"),
    path("agregar-productos/", views.agregar_productos, name="agregar-productos"),
    path("editar-producto/<int:id>/", views.editar_producto, name="editar-producto"),
    path("eliminar-producto/<int:id>/", views.eliminar_producto, name="eliminar-producto"),
]
