# Generated by Django 3.0.5 on 2020-04-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200418_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
