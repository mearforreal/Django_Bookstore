# Generated by Django 2.2 on 2019-12-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20191205_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]