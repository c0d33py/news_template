# Generated by Django 2.2.3 on 2019-12-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.URLField(max_length=250)),
            ],
        ),
    ]
