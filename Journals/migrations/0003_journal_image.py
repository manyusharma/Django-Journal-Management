# Generated by Django 2.1 on 2019-05-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journals', '0002_journal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
