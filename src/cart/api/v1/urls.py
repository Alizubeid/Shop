from django.urls import path
from .views import ProductAPIView,CheckOutCart

urlpatterns = [
    path("products/",ProductAPIView.as_view(),name="product-list-view-API"),
    path("checkout/",CheckOutCart.as_view(),name="checkout")
]
