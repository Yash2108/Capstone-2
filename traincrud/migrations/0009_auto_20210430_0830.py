# Generated by Django 3.1.7 on 2021-04-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traincrud', '0008_auto_20210430_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='TrainImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
