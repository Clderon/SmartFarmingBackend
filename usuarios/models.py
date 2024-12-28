from django.db import models
from core.models import  Estado
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    # Relación con Estado (Filtrar por categoría "Rol")
    estado = models.ForeignKey(
        Estado, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        limit_choices_to={'categoria': 'Rol'}
    )    
    
    class Meta:
        verbose_name = "rol"
        verbose_name_plural = "roles"
        db_table = "rol"
        ordering = ["-creado"]
    
    def __str__(self):
        return self.nombre



class Usuario(AbstractBaseUser):
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    genero = models.CharField(
        max_length=10,
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        default='O'
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.ForeignKey(
        Estado, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        limit_choices_to={'categoria': 'Usuario'}
    )
    
    USERNAME_FIELD = 'username'  # Usamos 'username' para la autenticación
    REQUIRED_FIELDS = ['email', 'nombres', 'apellido_paterno', 'apellido_materno', 'rol']

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        db_table = "usuario"
        ordering = ["-creado"]



class TipoNotificacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  
    descripcion = models.TextField(blank=True, null=True) 
    severidad = models.IntegerField(                       
        choices=[
            (1, "Baja"),
            (2, "Media"),
            (3, "Alta"),
            (4, "Urgente"),
            (5, "Crítica")
        ],
        default=1
    )     
    creado = models.DateTimeField(auto_now_add=True)       
    actualizado = models.DateTimeField(auto_now=True)      

    def __str__(self):
        return f"{self.nombre} (Severidad {self.severidad})"

    class Meta:
        verbose_name = "tipoNotificacion"
        verbose_name_plural = "tipoNotificaciones"
        db_table = "tipoNotificacion"
        ordering = ['-severidad', 'nombre']

class Notificacion(models.Model):
    mensaje = models.TextField()
    tipo_notificacion = models.ForeignKey(TipoNotificacion, on_delete=models.PROTECT)
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name="notificaciones_recibidas"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    link_accion = models.URLField(blank=True, null=True)

    # Relación con Estado (Filtrar por categoría "Notificacion")
    estado = models.ForeignKey(
        Estado,  # Relación con la tabla Estado
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'categoria': 'Notificacion'}
    )

    # La severidad se obtiene automáticamente del TipoNotificacion
    @property
    def severidad(self):
        return self.tipo_notificacion.severidad


    def __str__(self):
        return f"{self.tipo.nombre}: {self.mensaje[:30]}..."

    class Meta:
        verbose_name = "Notificacion"
        verbose_name_plural = "Notificaciones"
        db_table = "notificacion"
        ordering = ["-fecha"]
