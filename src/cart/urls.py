from django.urls import path
from .views import AddCartView, CompanyCartHistory,AddProductView,UpdateProductView

urlpatterns = [
    path("add_cart/<int:pk>/",AddCartView.as_view(),name="add_cart"),
    path("add_product/",AddProductView.as_view(),name="add_product"),
    path("<pk>/edit_product/",UpdateProductView.as_view(),name="update_product")
]
