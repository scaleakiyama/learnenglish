# Generated by Django 5.1.6 on 2025-02-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField(choices=[(1, '1 месяц'), (3, '3 месяца'), (6, '6 месяцев'), (12, '1 год')])),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
    ]
