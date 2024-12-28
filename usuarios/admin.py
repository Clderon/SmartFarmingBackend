from django.contrib import admin
from .models import Rol, Notificacion, TipoNotificacion, Usuario

# Register your models here.

class RolAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")
    
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ("last_login",)

admin.site.register(Rol, RolAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Notificacion)
admin.site.register(TipoNotificacion)