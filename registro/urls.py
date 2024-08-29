from django.urls import path, include
from .views import SignupPageView
# crear viewa acá

urlpatterns =  [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup",SignupPageView.as_view(),name="signup")
]