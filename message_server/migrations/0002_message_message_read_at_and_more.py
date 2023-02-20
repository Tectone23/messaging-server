# Generated by Django 4.1.6 on 2023-02-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_read_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='userbundle',
            name='identity_key',
            field=models.TextField(verbose_name='IdentityKey'),
        ),
        migrations.AlterField(
            model_name='userbundle',
            name='pre_key',
            field=models.TextField(verbose_name='PreKey'),
        ),
        migrations.AlterField(
            model_name='userbundle',
            name='pre_key_sig',
            field=models.TextField(verbose_name='PreKeySig'),
        ),
    ]