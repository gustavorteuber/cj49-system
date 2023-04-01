from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Usuario, Estoque, Pedido, Produto, Etiqueta
from core.serializers import (
    UsuarioSerializer,
    UsuarioCreateSerializer,
    EstoqueSerializer,
    PedidoSerializer,
    ProdutoSerializer,
    DetailProdutoSerializer,
    EtiquetaSerializer,
    DetailEstoqueSerializer
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["id"] = self.user.id
        data["email"] = self.user.email
        data["is_superuser"] = self.user.is_superuser

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return UsuarioCreateSerializer
        return UsuarioSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailProdutoSerializer
        return ProdutoSerializer


class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailEstoqueSerializer
        return EstoqueSerializer


class EtiquetaViewSet(ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer
    permission_classes = [AllowAny]


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [AllowAny]


@api_view(['PATCH'])
def atualizar_estoque(request):
    # Verifica se o pedido é PATCH
    if request.method == 'PATCH':
        # Aqui você pode escrever o código para atualizar o estoque
        # usando os dados enviados na requisição
        # Por exemplo:
        estoque = Estoque.objects.get(pk=1)
        estoque.coca = request.data.get('coca', estoque.coca)
        estoque.cerveja = request.data.get('cerveja', estoque.cerveja)
        estoque.hamburguer = request.data.get('hamburguer', estoque.hamburguer)
        estoque.save()
        # Retorna uma resposta de sucesso
        return Response({'message': 'Estoque atualizado com sucesso!'})
    else:
        # Se a requisição não for PATCH, retorna um erro 405
        return Response({'error': 'Método não permitido.'}, status=405)
