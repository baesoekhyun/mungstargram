# Generated by Django 4.2.6 on 2023-10-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_feed_profile_image_remove_feed_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
