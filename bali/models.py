from django.db import models

# Create your models here.

class AddNumber(models.Model):
    addNumber1 = models.IntegerField()
    addNumber2 = models.IntegerField()

    def __str__(self):
        return str(self.addNumber1)
