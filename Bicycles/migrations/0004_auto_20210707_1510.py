# Generated by Django 3.2.3 on 2021-07-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bicycles', '0003_alter_bsles_wheels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bsles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='frame',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='marks',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='type',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wheels',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
