from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Titulo')
    image = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    description = models.TextField(null=True, verbose_name='Descripcion')
    
    def __str__(self):
        fila = "Titulo: " + self.title 
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()