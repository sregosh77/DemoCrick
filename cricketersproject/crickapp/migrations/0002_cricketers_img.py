# Generated by Django 4.2.1 on 2023-06-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crickapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cricketers',
            name='img',
            field=models.ImageField(default='sai', upload_to='gallery'),
            preserve_default=False,
        ),
    ]