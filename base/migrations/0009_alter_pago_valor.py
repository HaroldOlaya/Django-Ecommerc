# Generated by Django 4.2.3 on 2023-09-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_pago_user_alter_pago_numerofactura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='valor',
            field=models.IntegerField(null=True),
        ),
    ]
