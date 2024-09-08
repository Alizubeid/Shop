from django.urls import path
from .views import ProductListView,CompanyListView,ProductCompanyListView,OwnerOrCustomerRegisterView,UserLoginView
from django.views.generic.base import TemplateView

urlpatterns = [
    path("",ProductListView.as_view(),name="root"),
    path("register/",OwnerOrCustomerRegisterView.as_view(),name="signup"),
    path("companies/",CompanyListView.as_view(),name="comanies"),
    path("company/<str:name>/products/",ProductCompanyListView.as_view(),name="company_products"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("profile/",ProductListView.as_view(),name="profile")
]
