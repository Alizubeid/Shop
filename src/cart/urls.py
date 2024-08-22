from django.urls import path
from .views import AddCartView

urlpatterns = [
    path("add_cart/<int:pk>/",AddCartView.as_view(),name="add_cart")
]
