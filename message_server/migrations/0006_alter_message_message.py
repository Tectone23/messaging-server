# Generated by Django 4.1.6 on 2023-02-22 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_server', '0005_alter_userbundle_identity_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.BinaryField(verbose_name='Message Body'),
        ),
    ]
