from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('usuarios/count/', UsuarioViewSet.as_view({'get': 'count_users'}), name='count_users'),
    path('usuarios/export_csv', UsuarioViewSet.as_view({'get': 'export_users_csv'}), name= 'export_users_csv'),
    path('usuarios/<int:pk>/update_user/', UsuarioViewSet.as_view({'put': 'update_user'}), name='update_user'),
]


urlpatterns += router.urls
