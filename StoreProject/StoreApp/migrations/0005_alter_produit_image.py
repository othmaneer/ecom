# Generated by Django 4.1.7 on 2023-04-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0004_alter_produit_nom_alter_user_mail_alter_user_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]