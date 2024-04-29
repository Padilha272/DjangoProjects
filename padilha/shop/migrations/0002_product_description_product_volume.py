# Generated by Django 5.0.4 on 2024-04-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
