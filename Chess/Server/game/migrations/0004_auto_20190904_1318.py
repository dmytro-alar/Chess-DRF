# Generated by Django 2.1.7 on 2019-09-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190902_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(default='invited', max_length=255),
        ),
    ]
