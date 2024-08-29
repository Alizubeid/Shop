from django.urls import path
from .views import ProductListView,CompanyListView

urlpatterns = [
    path("",ProductListView.as_view(),name="root"),
    path("companies/",CompanyListView.as_view(),name="comanies"),
    path("company/<str:name>/products/",ProductListView.as_view(),name="company_products")
]
