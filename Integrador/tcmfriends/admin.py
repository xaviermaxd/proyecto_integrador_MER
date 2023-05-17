from django.contrib import admin
from .models import Usuario, Conversacion, Mensaje, Publicacion, Reclamo, SolicitudAmistad
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","nombres","apellidos","email","carrera","ciclo","foto","descripcion")

class ConversacionAdmin(admin.ModelAdmin):
    list_display = ("id","persona1","persona2")

class MensajeAdmin(admin.ModelAdmin):
    list_display = ("id","id_user_envio","id_chat","contenido","fecha_mensaje","hora_mensaje")

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("id","fecha_publicacion","hora_publicacion","imagen","contenido")

class ReclamoAdmin(admin.ModelAdmin):
    list_display = ("id","id_user","asunto","contenido","imagen")

class SolicitudAdmin(admin.ModelAdmin):
    list_display = ("id","estado","fecha","hora")
     

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Conversacion,ConversacionAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Publicacion,PublicacionAdmin)
admin.site.register(Reclamo, ReclamoAdmin)
admin.site.register(SolicitudAmistad,SolicitudAdmin)