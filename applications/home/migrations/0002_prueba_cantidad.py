# Generated by Django 4.2.4 on 2023-08-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
