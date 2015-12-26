from django.db import models
from formacion.models import Grupo
from formador.models import Formador
from region.models import Region
from django.utils.encoding import smart_unicode

class CodigoMasivo(models.Model):
    codigo = models.BigIntegerField(unique=True)
    generado = models.BooleanField(editable=False,default=False)

    def __unicode__(self):
        return smart_unicode(self.codigo)

class ParticipanteEscuelaTicTrucho(models.Model):
    codigo_masivo = models.ForeignKey(CodigoMasivo)
    region = models.ForeignKey(Region)
    departamento = models.CharField(max_length=200,blank=True,null=True)
    municipio = models.CharField(max_length=200,blank=True,null=True)
    institucion = models.CharField(max_length=200,blank=True,null=True)
    grupo = models.ForeignKey(Grupo)
    formador = models.ForeignKey(Formador)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.BigIntegerField(unique=True,error_messages={'unique':"Este numero de identificacion ya ha sido registrado"})
    genero = models.CharField(max_length=100)
    nivel_educativo = models.CharField(max_length=100,blank=True,null=True)
    telefono = models.CharField(blank=True,max_length=100,null=True)
    correo = models.EmailField(blank=True,max_length=200,null=True)
    poblacion = models.CharField(blank=True,max_length=200,null=True)
    codigo_anspe = models.CharField(blank=True,max_length=200,null=True)
    tipo_proyecto = models.CharField(blank=True,max_length=200,null=True)
    grupo_conformacion = models.CharField(blank=True,max_length=200,null=True)

    def __unicode__(self):
        return smart_unicode(self.cedula)

class CargasMasivas(models.Model):
    archivo = models.FileField(upload_to="Cargas Masivas/Escuela TIC/Adicionales/")

    def __unicode__(self):
        return smart_unicode(self.id)

class Nivel1_Sesion1_1(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_2(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_3(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_4(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_5(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_6(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_7(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_8(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_9(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_10(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_11(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_12(models.Model):
    respuesta = models.CharField(max_length=5000)

    def __unicode__(self):
        return smart_unicode(self.respuesta)
class Nivel1_Sesion1_REDA(models.Model):
    recurso = models.CharField(max_length=200)
    portal = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __unicode__(self):
        return smart_unicode(self.recurso)