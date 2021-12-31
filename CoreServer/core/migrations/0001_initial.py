# Generated by Django 4.0 on 2021-12-30 21:29

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_name', models.CharField(help_text='Banned player name', max_length=32)),
                ('datetime_start', models.DateTimeField(help_text='Ban start date/time')),
                ('datetime_end', models.DateTimeField(help_text='Ban expiry date/time')),
                ('issued_by', models.CharField(help_text='Name of the issuing admin', max_length=32)),
                ('reason', models.TextField(help_text='Reason for the  ban to be issued')),
                ('variant', models.TextField(choices=[('PM', 'Permanent ban'), ('HD', 'Hard ban'), ('ST', 'Soft ban')], default='HD', help_text='Type of ban', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dnd_beyond_link', models.URLField(blank=True, help_text='Link to character sheet on D&D Beyond')),
                ('forewarning', models.TextField(blank=True, help_text='Warnings of shenanigans, or notes for DM')),
            ],
        ),
        migrations.CreateModel(
            name='DM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_name', models.CharField(help_text='Discord username', max_length=32)),
                ('name', models.CharField(help_text="DM's chosen alias or handle", max_length=64)),
                ('description', models.TextField(help_text='Flavour text / details to show')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='User defined game name', max_length=128)),
                ('module', models.CharField(blank=True, help_text='AL module code', max_length=32)),
                ('realm', models.TextField(choices=[('FRS', 'Forgotten Realms'), ('WLD', 'Wildemount'), ('EBR', 'Eberron'), ('RMH', 'Misthunters'), ('STX', 'Strixhaven'), ('RAV', 'Ravnica'), ('OTH', 'Any other setting')], default='FRS', help_text='Game setting', max_length=3)),
                ('variant', models.TextField(choices=[('RAL', 'Resident Adventurers League'), ('GAL', 'Guest DM Adventurers League'), ('EAL', 'Epic Adventurers League'), ('NAL', 'Non-AL One Shot'), ('CMP', 'Campaign')], default='RAL', help_text='Game type', max_length=3)),
                ('description', models.TextField(blank=True, help_text='Description of this game or flavour text')),
                ('max_players', models.IntegerField(default=6, help_text='Max players for this game')),
                ('level_min', models.IntegerField(default=1, help_text='Minumum starting level')),
                ('level_max', models.IntegerField(default=4, help_text='Maximum player level')),
                ('warnings', models.TextField(blank=True, help_text='Content warnings or advisories')),
                ('status', models.TextField(choices=[('CAN', 'Cancelled'), ('DRF', 'Draft'), ('PND', 'Pending'), ('PRT', 'Priority'), ('REL', 'Released')], default='DRF', help_text='Game status')),
                ('channel', models.CharField(blank=True, help_text='Discord channel to use for this game', max_length=32)),
                ('streaming', models.BooleanField(default=False, help_text='Game is streaming or not')),
                ('datetime_release', models.DateTimeField(help_text='Date/Time game is released for signups')),
                ('datetime_open_release', models.DateTimeField(help_text='Date/Time game is released to gen-pop')),
                ('datetime', models.DateTimeField(help_text='Date/Time game is starting')),
                ('length', models.DurationField(help_text='Planned duration of game')),
                ('dm', models.ForeignKey(help_text='Dungeon Master for this game', on_delete=django.db.models.deletion.CASCADE, related_name='games', to='core.dm')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standby', models.BooleanField(default=False, help_text='If player is a standby player')),
                ('waitlist', models.IntegerField(help_text='Position in queue for place in game')),
                ('discord_name', models.CharField(help_text='Discord username', max_length=32)),
                ('character', models.ForeignKey(help_text='Character info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.character')),
                ('game', models.ForeignKey(help_text='Game user is playing in', on_delete=django.db.models.deletion.CASCADE, related_name='players', to='core.game')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('discord_name', models.CharField(help_text='Discord username', max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]