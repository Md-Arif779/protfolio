# Generated by Django 3.2.5 on 2021-11-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
