# Generated by Django 4.0 on 2021-12-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenoms', models.CharField(max_length=255)),
                ('contact', models.CharField(blank=True, max_length=16)),
            ],
            options={
                'verbose_name': '√Čtudiant',
                'verbose_name_plural': '√Čtudiants',
                'db_table': 'core_etudiant',
            },
        ),
    ]
