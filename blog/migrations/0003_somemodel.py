# Generated by Django 3.2.20 on 2023-08-19 21:27

from django.db import migrations, models
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230816_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_summernote.fields.SummernoteTextField()),
            ],
        ),
    ]