# Generated by Django 4.2.5 on 2023-09-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpage',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Записи главной страницы'},
        ),
        migrations.AddField(
            model_name='mainpage',
            name='slimage',
            field=models.ImageField(null=True, upload_to='main/static/main/images/banner/'),
        ),
    ]
