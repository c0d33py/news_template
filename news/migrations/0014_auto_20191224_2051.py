# Generated by Django 2.2.3 on 2019-12-24 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_article_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Cat',
        ),
    ]
