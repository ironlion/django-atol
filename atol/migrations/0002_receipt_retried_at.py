# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-13 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='retried_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата повторной инициализации чека в системе оператора'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='status',
            field=models.CharField(choices=[('created', 'Ожидает инициации в системе оператора'), ('initiated', 'Иницирован в системе оператора'), ('retried', 'Повторно иницирован в системе оператора'), ('received', 'Получен от оператора'), ('no_email_phone', 'Отсутствует email/phone'), ('failed', 'Ошибка')], default='created', max_length=16, verbose_name='Статус чека'),
        ),
    ]