# Generated by Django 3.0 on 2020-04-13 13:32

from django.db import migrations, models
# import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191212_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField()
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(
                default='default.jpg', upload_to='post_pics'),
        ),
    ]
