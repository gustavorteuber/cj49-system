from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from core.views import (
    UsuarioViewSet,
    MyTokenObtainPairView,
    EstoqueViewSet,
    PedidoViewSet,
    ProdutoViewSet,
    EtiquetaViewSet,
    atualizar_estoque
)

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'pedido', PedidoViewSet)
router.register(r'etiqueta', EtiquetaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("media/", include(uploader_router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("patchEstoque/", atualizar_estoque, name="atualizar_estoque"),
]
urlpatterns += static(settings.MEDIA_ENDPOINT,
                      document_root=settings.MEDIA_ROOT)
