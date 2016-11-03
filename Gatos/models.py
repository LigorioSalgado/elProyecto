from django.db import models

SEXO_CHOICES= (
		("M","Masculino"),
		("F", "Femenino")
	)

# Create your models here.
class Comida(models.Model):
	
	#Attributes
	tipo = models.CharField(max_length=25, blank=False, null=False)
	compra = models.DateField(auto_now_add=True)
	caducidad = models.DateField()

	def __str__(self):
		return "Comida {0} caduca el {1}".format(self.tipo, str(self.caducidad))

class Gato(models.Model):

    class Meta:
        verbose_name = "Gato"
        verbose_name_plural = "Gatos"

    #Attributes
    name = models.CharField(max_length=10, blank=False, null=False)
    age = models.IntegerField(blank=True, null=False, default=0)
    callejero = models.BooleanField(default=False)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)

    #Relation
    comida = models.ForeignKey(Comida, related_name='gato_comida')

    def __str__(self):
        return self.name

