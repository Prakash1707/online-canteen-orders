# Generated by Django 2.2.5 on 2019-09-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20190925_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('typeof', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
