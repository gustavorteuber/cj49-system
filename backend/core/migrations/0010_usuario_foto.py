# Generated by Django 4.1.7 on 2023-03-03 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('core', '0009_etiqueta'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uploader.image'),
        ),
    ]