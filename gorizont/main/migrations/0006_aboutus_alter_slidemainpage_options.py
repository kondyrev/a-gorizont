# Generated by Django 4.2.5 on 2023-09-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_slidemainpage_delete_mainpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='текст')),
            ],
            options={
                'verbose_name': 'текст О НАС',
            },
        ),
        migrations.AlterModelOptions(
            name='slidemainpage',
            options={'verbose_name': 'Главный слайдер', 'verbose_name_plural': 'Слайды главной страницы'},
        ),
    ]