# Generated by Django 4.1.7 on 2023-03-03 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='etiqueta',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.produto'),
            preserve_default=False,
        ),
    ]
