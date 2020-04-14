# Generated by Django 3.0.3 on 2020-04-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Название домена (ex. www.google.com)')),
                ('path', models.CharField(max_length=225, verbose_name='Путь к проекту')),
                ('port', models.CharField(max_length=120, verbose_name='Порт проекта')),
                ('status', models.PositiveIntegerField(choices=[(0, 'Не активен'), (1, 'Активен')], default=0, verbose_name='Статус сайта')),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Сайты',
            },
        ),
    ]
