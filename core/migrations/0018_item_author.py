# Generated by Django 2.2 on 2019-12-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20191205_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]