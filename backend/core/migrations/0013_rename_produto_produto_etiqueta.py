# Generated by Django 4.1.7 on 2023-03-25 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_etiqueta_produto_produto_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='produto',
            new_name='etiqueta',
        ),
    ]
