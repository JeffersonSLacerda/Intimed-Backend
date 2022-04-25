from rest_framework import serializers

from medicar.models import Doctor, Schedule

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields = ['id', 'name', 'crm', 'email']
        
class ScheduleSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    class Meta:
        model= Schedule
        fields = ['id', 'day', 'hour', 'created_at', 'doctor']