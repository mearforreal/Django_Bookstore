# Generated by Django 2.2 on 2019-12-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20191205_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]