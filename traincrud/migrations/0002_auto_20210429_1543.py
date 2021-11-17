# Generated by Django 3.1.7 on 2021-04-29 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traincrud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='Goods',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='train',
            name='Passenger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='train',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='train',
            name='dateoflauch',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='train',
            name='train_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]