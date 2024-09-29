from django.urls import path
from customers.views import CustomerRegisterView

urlpatterns = [
    path("customer/",CustomerRegisterView.as_view(),name="reg-customer"),
]
