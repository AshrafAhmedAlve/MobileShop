# Generated by Django 5.0.3 on 2024-11-22 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mobile_images/'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
