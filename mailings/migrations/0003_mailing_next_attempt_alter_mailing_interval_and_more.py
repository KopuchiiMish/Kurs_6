# Generated by Django 4.2.6 on 2023-11-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0002_logs_rename_owner_mailing_user_mailing_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='next_attempt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последней отправки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='interval',
            field=models.CharField(choices=[('every_minute', 'Каждую минуту'), ('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], default='daily', max_length=15, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('created', 'Создана'), ('enabled', 'Активна'), ('disabled', 'Неактивна')], default='enabled', max_length=8, verbose_name='Статус рассылки'),
        ),
    ]
