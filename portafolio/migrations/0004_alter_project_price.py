# Generated by Django 4.2 on 2023-09-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0003_rename_producto_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.IntegerField(max_length=20, verbose_name='Precio'),
        ),
    ]