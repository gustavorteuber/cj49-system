
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from core.views import (
    UsuarioViewSet,
    MyTokenObtainPairView, BoletosList, BoletosDetail
)

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('boletos/', BoletosList.as_view(), name='boletos-list'),
    path('boletos/<int:pk>/', BoletosDetail.as_view(), name='boletos-detail'),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
