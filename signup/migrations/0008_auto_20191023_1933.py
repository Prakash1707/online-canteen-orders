# Generated by Django 2.2.5 on 2019-10-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_cart_transcid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='transcid',
            field=models.CharField(default='NULL', max_length=40),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transactionId',
            field=models.CharField(max_length=40),
        ),
    ]
