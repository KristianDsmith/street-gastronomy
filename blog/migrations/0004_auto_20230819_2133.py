# Generated by Django 3.2.20 on 2023-08-19 21:33

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_somemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SomeModel',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
