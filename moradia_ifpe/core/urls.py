from django.urls import path, include
from moradia_ifpe.core.views import CustomLoginView, CustomLogoutView, NotPermissionView, CustomRegisterView

urlpatterns = [
    path("", CustomLoginView.as_view(), name='login'),
    path("registro/", CustomRegisterView.as_view(), name='register'),
    path("dashboard/", include('moradia_ifpe.dashboard.urls')),
    path("logout/", CustomLogoutView.as_view(), name='logout'),
    path("error/403/", NotPermissionView.as_view(), name='not_permission'),
]
