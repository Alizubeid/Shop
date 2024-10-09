from django.urls import path
from .views import AddCartView, CompanyCartHistory,AddProductView,UpdateProductView,DiscountChoise,AddProductDiscount,AddCategoryDiscount,ProductItemView,ThankYouView,CartHistoryView

urlpatterns = [
    path("add_cart/<int:pk>/",AddCartView.as_view(),name="add_cart"),
    path("add_product/",AddProductView.as_view(),name="add_product"),
    path("<pk>/edit_product/",UpdateProductView.as_view(),name="update_product"),
    path("discount/",DiscountChoise.as_view(),name="set-discount"),
    path("discount/product/",AddProductDiscount.as_view(),name="discount-product"),
    path("discount/category/",AddCategoryDiscount.as_view(),name="discount-category"),
    path("cart/",ProductItemView.as_view(),name="cart"),
    path("thankyou/",ThankYouView.as_view(),name="thankyou"),
    path("history/",CartHistoryView.as_view(),name="history")
]
