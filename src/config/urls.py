"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView,LogoutView




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",  include("website.urls")),
    path("signup/",include("accounts.urls")),
    path("api/",include("cart.api.v1.urls")),
    path("cart/",include("cart.urls")),
    path("login/",LoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page="login"),name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

