# Generated by Django 5.0 on 2023-12-16 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('team_name', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'rankings',
                'ordering': ('ranking',),
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1_score', models.IntegerField()),
                ('team_2_score', models.IntegerField()),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_team_1', to='ranking.team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_team_2', to='ranking.team')),
            ],
            options={
                'verbose_name_plural': 'games',
            },
        ),
    ]
