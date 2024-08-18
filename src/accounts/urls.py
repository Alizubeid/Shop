from django.urls import path,include
from customers.urls import urlpatterns as customers_urls
from vendors.urls import urlpatterns as vendors_urls
urlpatterns = []
urlpatterns+=customers_urls
urlpatterns+=vendors_urls