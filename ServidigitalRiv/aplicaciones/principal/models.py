from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Persona(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=25)
    apellido= models.CharField(max_length=25)
    email= models.EmailField(max_length=100)
    estado=models.BooleanField('Estado', default=True)
    

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField('Nombre del Autor',max_length=255, null = False, blank = False)
    apellido= models.CharField('Apellidos del Autor',max_length=255, null = False, blank = False)
    facebook= models.URLField('Facebook', null = True, blank= True)
    twitter= models.URLField('Twitter', null = True, blank= True)
    instagram= models.URLField('Instagram', null = True, blank= True)
    web= models.URLField('Web', null = True, blank= True)
    correo= models.EmailField('Correo Electrónico', blank= False , null= False)
    estado=models.BooleanField('Estado', default=True)
    fecha_creacion=models.DateField('Fecha de creacion', auto_now= False, auto_now_add=True)
    
    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'
        ordering=['nombre', 'apellido']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=25)
    fecha_creacion=models.DateField('Fecha de creacion', auto_now= True, auto_now_add=False)
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateTimeField('Fecha de cración', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Titulo'
        verbose_name_plural='Titulos'
        ordering=['fecha_creacion']

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre= models.CharField('Nombre de la categoria', max_length=100, null = False, blank = False)
    estado=models.BooleanField('Activo/Desactivo', default=True)
    fecha_creacion = models.DateTimeField('Fecha de cración', auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= ' Categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo= models.CharField('Título', max_length=100, null = False, blank = False)
    slug= models.CharField('Slug', max_length=100, null = False, blank = False)
    descripcion= models.CharField('Descripción', max_length=255, null = False, blank = False)
    #contenido = models.RichTextField('Contenido')
    imagen = models.URLField(max_length = 255, blank= False, null= False)
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/no Publicado', default=True)
    fecha_creacion= models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

        def __str__(self):
                return self.titulo
    
    




