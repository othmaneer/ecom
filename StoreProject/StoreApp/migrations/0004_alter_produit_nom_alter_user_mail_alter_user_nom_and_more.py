# Generated by Django 4.1.7 on 2023-04-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0003_alter_user_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='nom',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nom',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='prenom',
            field=models.CharField(max_length=255),
        ),
    ]
