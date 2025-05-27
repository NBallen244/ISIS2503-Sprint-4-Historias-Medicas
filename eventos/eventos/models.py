from django.db import models


class Evento(models.Model):
    fecha=models.DateField(auto_now_add=True)
    historiaPaciente=models.IntegerField(null=False, default=None)
    especialidad=models.CharField(max_length=100, default="Consulta General")
    comentarios=models.TextField(default=None)
    
    def __str__(self):
        return '{}'.format(self.historiaPaciente.id+' - '+self.fecha.strftime('%Y-%m-%d')+' - '+self.especialidad[0:4])
