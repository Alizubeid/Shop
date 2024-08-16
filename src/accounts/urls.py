from django.urls import path,include
urlpatterns = [
    path("reg_customer/",include("customers.urls")),
]