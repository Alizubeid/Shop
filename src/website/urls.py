from django.urls import path
from .views import (
    ProductListView,
    CompanyListView,
    ProductCompanyListView,
    OwnerOrCustomerRegisterView,
    UserLoginView,
    ProfileUserView,
    ProfileUserUpdateView,
    AddressUserUpdateView
)
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", ProductListView.as_view(), name="root"),
    path("register/", OwnerOrCustomerRegisterView.as_view(), name="signup"),
    path("companies/", CompanyListView.as_view(), name="comanies"),
    path(
        "company/<str:name>/products/",
        ProductCompanyListView.as_view(),
        name="company_products",
    ),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", ProfileUserView.as_view(), name="profile"),
    path("profile/edit/",ProfileUserUpdateView.as_view(),name="update_profile"),
    path("address/edit/",AddressUserUpdateView.as_view(),name="update_address"),
]
