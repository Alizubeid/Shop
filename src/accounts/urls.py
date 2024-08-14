from django.urls import path
from accounts.views import SignUpView, ProfileFormView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileFormView.as_view(), name="profile"),
]