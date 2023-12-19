# Generated by Django 5.0 on 2023-12-19 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_alter_games_team_1_alter_games_team_2_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='ranking',
            name='team_name',
        ),
        migrations.AddField(
            model_name='ranking',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ranking.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='games',
            name='team_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_team_1', to='ranking.team'),
        ),
        migrations.AlterField(
            model_name='games',
            name='team_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_team_2', to='ranking.team'),
        ),
    ]
