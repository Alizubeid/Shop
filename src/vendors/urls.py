from django.urls import path
from vendors.views import OwnerRegisterView,ManagerRegisterView,OperatorRegisterView

urlpatterns = [
    path("owner/", OwnerRegisterView.as_view(), name="reg-owner"),
    path("manager/", ManagerRegisterView.as_view(), name="reg-manager"),
    path("operator/", OperatorRegisterView.as_view(), name="reg-operator"),
]
