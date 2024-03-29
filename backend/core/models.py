from django.contrib.auth.models import AbstractUser
from django.db import models
from uploader.models import Image
from django.dispatch import receiver
from django.db.models.signals import post_save


class Usuario(AbstractUser):
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_totem = models.BooleanField(default=False)


# class Estoque(models.Model):
#     coca = models.IntegerField()
#     cerveja = models.IntegerField()
#     hamburguer = models.IntegerField()


# class Pedido(models.Model):
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     coca = models.IntegerField()
#     cerveja = models.IntegerField()
#     hamburguer = models.IntegerField()
#     data = models.DateTimeField(auto_now_add=True)


# @receiver(post_save, sender=Pedido)
# def atualizar_estoque(sender, instance, created, **kwargs):
#     if created:
#         estoque = Estoque.objects.first()
#         estoque.coca -= instance.coca
#         estoque.cerveja -= instance.cerveja
#         estoque.hamburguer -= instance.hamburguer
#         estoque.save()


class Etiqueta(models.Model):
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"

    def baixar(self, quantidade):
        if quantidade > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque")
        self.quantidade -= quantidade
        self.save()


class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} - {self.data}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        estoque = Estoque.objects.get(produto=self.produto)
        estoque.baixar(self.quantidade)
