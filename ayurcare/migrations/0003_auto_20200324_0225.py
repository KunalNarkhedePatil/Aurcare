# Generated by Django 2.2.6 on 2020-03-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ayurcare', '0002_auto_20200323_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='address',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='c_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='city',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='product',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ayurcare.Profile'),
        ),
    ]
