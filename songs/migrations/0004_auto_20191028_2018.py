# Generated by Django 2.2.3 on 2019-10-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20191028_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(upload_to='media/'),
        ),
    ]
