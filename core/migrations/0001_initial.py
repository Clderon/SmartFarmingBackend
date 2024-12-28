# Generated by Django 4.2.17 on 2024-12-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.CharField(choices=[('Usuario', 'Usuario'), ('Notificacion', 'Notificación'), ('Suscripcion', 'Suscripción'), ('Transaccion', 'Transacción'), ('Analisis', 'Análisis'), ('Sesion', 'Sesión')], max_length=50)),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
                'db_table': 'estado',
                'ordering': ['-creado'],
            },
        ),
    ]