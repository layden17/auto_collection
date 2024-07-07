from django.db import models
from django.core.exceptions import ValidationError

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def clean(self):
        if not self.brand.isalpha():
            raise ValidationError({'brand': "La marque doit contenir uniquement des lettres."})

        if self.year < 1900 or self.year > 2100:
            raise ValidationError({'year': "L'année doit être comprise entre 1900 et 2100."})

        if self.price < 0:
            raise ValidationError({'price': "Le prix ne peut pas être négatif."})
