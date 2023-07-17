from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    generation = models.IntegerField()

    def __str__(self):
        return f'{self.id} // {self.brand}'