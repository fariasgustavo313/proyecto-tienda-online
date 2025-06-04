from django.db import models

class Remera(models.Model):
    verbose_name_plural = "Remeras"
    
    TALLES = [
        (1, "XS"),
        (2, "S"),
        (3, "M"),
        (4, "L"),
        (5, "XL"),
        (6, "XXL"),
    ]
    
    GENEROS = [
        (1, "Hombre"),
        (2, "Mujer"),
        (3, "Unisex")
    ]
    LISA = [
        (True, "Si"),
        (False, "No")
    ]
    
    marca = models.CharField("Marca", max_length=50)
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    color = models.CharField("Color", max_length=50)
    lisa = models.BooleanField("Lisa", choices=LISA)
    genero = models.PositiveSmallIntegerField("Genero", choices=GENEROS)
    imagen = models.ImageField(upload_to="remeras/", null=True, blank=True)

    
    def __str__(self):
        titulo_remera = f"{self.marca} {self.color} {self.get_talle_display()}"
        return titulo_remera