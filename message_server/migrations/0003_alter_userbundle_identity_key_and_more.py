# Generated by Django 4.1.6 on 2023-02-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_server', '0002_message_message_read_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbundle',
            name='identity_key',
            field=models.BinaryField(verbose_name='IdentityKey'),
        ),
        migrations.AlterField(
            model_name='userbundle',
            name='one_time_pre_key',
            field=models.BinaryField(verbose_name='OneTimePreKey'),
        ),
        migrations.AlterField(
            model_name='userbundle',
            name='pre_key',
            field=models.BinaryField(verbose_name='PreKey'),
        ),
        migrations.AlterField(
            model_name='userbundle',
            name='pre_key_sig',
            field=models.BinaryField(verbose_name='PreKeySig'),
        ),
    ]
