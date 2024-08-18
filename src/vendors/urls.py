from django.urls import path
from vendors.views import OwnerCreateView, ManagerCreateView, OperatorCreateView

urlpatterns = [
    path("owner/", OwnerCreateView.as_view(), name="reg-owner"),
    path("manager/", ManagerCreateView.as_view(), name="reg-manager"),
    path("operator/", OperatorCreateView.as_view(), name="reg-operator"),
]
