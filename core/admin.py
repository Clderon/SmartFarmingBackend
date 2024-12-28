from django.contrib import admin
from .models import Estado

# Register your models here.


class EstadoAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")
    
admin.site.register(Estado, EstadoAdmin)