# Generated by Django 4.0 on 2022-01-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_snipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snipped',
            field=models.CharField(max_length=255),
        ),
    ]
