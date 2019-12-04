# Generated by Django 2.2 on 2019-12-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('H', 'Horror'), ('R', 'Romance'), ('F', 'Fantasy')], default='H', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('p', 'primary'), ('s', 'sencondary'), ('d', 'danger')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]
