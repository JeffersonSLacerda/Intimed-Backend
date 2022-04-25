import datetime
from django.db import models
from django.core.exceptions import ValidationError

class Doctor(models.Model):
    crm = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.crm, self.name)
    
    class Meta:
        db_table='doctor'
    
class Schedule(models.Model):
    day = models.DateField()
    hour = models.TimeField()
    
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}/{} - {}'.format(self.day, self.hour, self.doctor)

    def clean(self):
        if self.day < datetime.date.today():
            raise ValidationError({'day': "Dias passados não são válidos"})
        check = Schedule.objects.filter(day = self.day, doctor = self.doctor)
        if len(check) > 0:
            raise ValidationError({'day': 'Data já com agendamento'})
        

    class Meta:
        db_table='schedule'