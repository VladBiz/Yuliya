# Generated by Django 3.2 on 2021-06-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210531_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='money',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='money',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='balance'),
            preserve_default=False,
        ),
    ]
