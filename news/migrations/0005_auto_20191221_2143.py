# Generated by Django 2.2.3 on 2019-12-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20191221_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='P_content',
            field=models.CharField(max_length=1000),
        ),
    ]
