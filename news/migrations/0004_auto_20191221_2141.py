# Generated by Django 2.2.3 on 2019-12-21 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20191221_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='P_content',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]