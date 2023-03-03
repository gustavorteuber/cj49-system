# Generated by Django 4.1.7 on 2023-03-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_pedido_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
