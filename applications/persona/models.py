from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)


    class Meta():
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 




class Empleado(models.Model):
    """ Modelo para tabla de empleados    """
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO')
    )
    #contador
    #administrador
    #economista
    #otro
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    ## se agrega este atributo al modelos
    full_name = models.CharField('nombres completos', max_length=120, blank=True, null=True)
    #aqui creamos un apartado donde se puede elegir el tipo de trabajo en la bse de datos del administrador
    job = models.CharField('trabajo', max_length=1, choices=JOB_CHOICES )
    #aqui creamos la relacion entra la base de datos de los departamentos y los empleados
    #relacion de uno a muchos
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    avatar = models.ImageField( upload_to='empleado',blank=True, null=True )
    
    
    
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    class Meta():
        verbose_name = 'Empleados'
        verbose_name_plural = 'Empleados de la empresa'
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name    