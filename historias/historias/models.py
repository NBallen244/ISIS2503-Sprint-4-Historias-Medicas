from django.db import models

class Historia(models.Model):
    paciente = models.CharField(max_length=100)
    cc=models.IntegerField()

    def __str__(self):
        return str(self.id)