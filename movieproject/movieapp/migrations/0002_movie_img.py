# Generated by Django 3.2.10 on 2021-12-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='image_name', upload_to='gallery'),
            preserve_default=False,
        ),
    ]