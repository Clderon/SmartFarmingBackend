from django.db import models

# Create your models here.
class Estado(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    # Nueva columna para la categoría del estado
    categoria = models.CharField(max_length=50, choices=[
        ('Usuario', 'Usuario'),
        ('Notificacion', 'Notificación'),
        ('Suscripcion', 'Suscripción'),
        ('Transaccion', 'Transacción'),
        ('Analisis', 'Análisis'),
        ('Sesion', 'Sesión'),
        ('Rol', 'Rol'),
    ])
    
    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"
        db_table = "estado"
        ordering = ["-creado"]
    
    def __str__(self):
        return f"{self.nombre} ({self.categoria})"