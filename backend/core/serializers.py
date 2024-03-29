from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Usuario, Estoque, Pedido, Produto, Etiqueta


class UsuarioSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "is_totem",
            "email",
            "username",
            "password",
        )

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        password = args.get("password")
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("esse email já está cadastrado")}
            )
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("esse nome de usuario já está em uso")}
            )

        return args


class UsuarioCreateSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "is_totem",
            "email",
            "username",
            "password",
        )

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        password = args.get("password")
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("esse email já está cadastrado")}
            )
        if Usuario.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("esse nome de usuario já está em uso")}
            )
        return super().validate(args)

    def create(self, validated_data):
        newUser = Usuario.objects.create_user(**validated_data)
        newUser.foto = None
        newUser.save()
        return newUser


class EstoqueSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Estoque
        read_only_fields = ("id",)
        fields = "__all__"

class DetailEstoqueSerializer(ModelSerializer):
    class Meta:
        model = Estoque
        fields = "__all__"
        depth = 1


class ProdutoSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Produto
        read_only_fields = ("id",)
        fields = "__all__"


class DetailProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1


class EtiquetaSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Etiqueta
        read_only_fields = ("id",)
        fields = "__all__"


class PedidoSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Pedido
        read_only_fields = ("id",)
        fields = "__all__"
