# Generated by Django 3.0.5 on 2020-05-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20200523_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='name',
            field=models.CharField(default='image', max_length=255, verbose_name='Название'),
        ),
    ]
