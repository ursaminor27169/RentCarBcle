# Generated by Django 3.2.5 on 2021-07-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bicycles', '0004_auto_20210707_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='bsles',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
