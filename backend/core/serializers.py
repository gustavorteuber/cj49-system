from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Usuario, Boletos

class UsuarioSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
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
        if password != args.get("password_confirmation"):
            raise serializers.ValidationError(
                {"password": ("as senhas não conferem")}
            )
        return args


class UsuarioCreateSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    password_confirmation = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = Usuario
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
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
        if password != args.get("password_confirmation"):
            raise serializers.ValidationError(
                {"password": ("as senhas não são iguais")}
            )
        return super().validate(args)

    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        newUser = Usuario.objects.create_user(**validated_data)
        newUser.foto = None
        newUser.save()
        return newUser

class BoletosSerializer(ModelSerializer):
    class Meta:
        model = Boletos
        fields = "__all__"
