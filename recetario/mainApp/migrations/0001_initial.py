# Generated by Django 4.1.2 on 2022-10-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreReceta', models.CharField(max_length=300, verbose_name='Nombre Receta')),
                ('ingredientes', models.TextField(verbose_name='Ingredientes Receta')),
                ('pasos', models.TextField(verbose_name='Pasos Receta')),
                ('imagenReceta', models.ImageField(upload_to='images/', verbose_name='Imagen Receta')),
                ('autor', models.CharField(max_length=30, verbose_name='Autor Receta')),
            ],
        ),
    ]
