# Generated by Django 3.2.5 on 2021-07-26 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='base',
            options={'ordering': ('-synced',)},
        ),
        migrations.AddField(
            model_name='base',
            name='synced',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='base',
            name='hn_deleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
