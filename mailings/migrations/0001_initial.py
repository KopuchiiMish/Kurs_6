# Generated by Django 4.2.6 on 2023-10-25 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(verbose_name='Тема рассылки')),
                ('body', models.TextField(verbose_name='Содержание рассылки')),
                ('customers', models.ManyToManyField(to='customers.customer', verbose_name='Клиенты')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата рассылки')),
                ('interval', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], default='daily', max_length=7, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('created', 'СОЗДАНА'), ('enabled', 'АКТИВНА'), ('disabled', 'НЕАКТИВНА')], default='active', max_length=8, verbose_name='Статус рассылки')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailing')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройки рассылки',
            },
        ),
    ]
