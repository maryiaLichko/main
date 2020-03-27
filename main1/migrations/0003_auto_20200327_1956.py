# Generated by Django 2.2.9 on 2020-03-27 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main1', '0002_score_teams_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_captain', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='teams',
            name='members',
        ),
        migrations.AddField(
            model_name='tasks',
            name='scores',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main1.Teams'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
