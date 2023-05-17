from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    carrera = models.CharField(max_length=50)
    ciclo = models.CharField(max_length=10)
    foto = models.ImageField()
    descripcion = models.CharField(max_length=250)

class Conversacion(models.Model):
    persona1 = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    persona2 = models.CharField(max_length=50)

class Mensaje(models.Model):
    id_user_envio = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_chat = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=300)
    fecha_mensaje = models.DateField() 
    hora_mensaje = models.TimeField()

class Publicacion(models.Model):
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField() 
    hora_publicacion = models.TimeField()
    imagen = models.ImageField()
    contenido = models.CharField(max_length=400)

class Reclamo(models.Model):
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=50)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField()

class SolicitudAmistad(models.Model):
    id_usuario_envio = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    fecha = models.DateField()
    hora = models.TimeField()