from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    curso = models.CharField(max_length=50)
    correo = models.EmailField()


class Pregunta(models.Model):
    enunciado = models.TextField()
    idPregunta = models.IntegerField()
    respuesta_correcta = models.CharField()
    siguiente_pregunta_correcta = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='preguntas_correctas'
    )
    siguiente_pregunta_incorrecta = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='preguntas_incorrectas'
    )


class Respuesta(models.Model):
    idRespuesta = models.IntegerField()
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name='respuestas'
    )
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='respuestas'
    )
    respuesta = models.CharField(max_length=255)

# Create your models here.
