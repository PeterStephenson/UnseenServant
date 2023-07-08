# Generated by Django 4.2.3 on 2023-07-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_rank_discord_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='discord_discriminator',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='discord_id',
            field=models.CharField(blank=True, help_text='Discord ID of user', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='discord_name',
            field=models.CharField(blank=True, help_text='Discord username', max_length=32, null=True),
        ),
    ]