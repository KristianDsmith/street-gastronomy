# Generated by Django 3.2.20 on 2023-08-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
