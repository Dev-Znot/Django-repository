# Generated by Django 4.2.9 on 2024-01-21 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cad_livros',
            new_name='livros',
        ),
    ]