# Generated by Django 4.2.17 on 2024-12-22 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Rol',
        ),
        migrations.AlterModelTable(
            name='rol',
            table='rol',
        ),
    ]
