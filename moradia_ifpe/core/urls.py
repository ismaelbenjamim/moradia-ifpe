from django.urls import path

from moradia_ifpe.core.views import CustomLoginView, DashboardView, CustomLogoutView, NotPermissionView, \
    ImportSpreadSheetView

urlpatterns = [
    path("", CustomLoginView.as_view(), name='login'),
    path("dashboard/", DashboardView.as_view(), name='dashboard'),
    path("logout/", CustomLogoutView.as_view(), name='logout'),
    path("error/403/", NotPermissionView.as_view(), name='not_permission'),
    path("dashboard/import-spreadsheet/", ImportSpreadSheetView.as_view(), name='import_spreadsheet'),
]
