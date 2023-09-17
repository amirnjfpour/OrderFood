from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import RegisterView, AddAdminView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("refresh-token/", TokenRefreshView.as_view(), name="refresh_token"),
    path("add-admin/", AddAdminView.as_view(), name="add_admin"),
]
