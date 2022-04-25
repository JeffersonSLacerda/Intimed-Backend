import datetime
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from medicar.models import Doctor, Schedule
from medicar.serializer import DoctorSerializer, ScheduleSerializer

class DoctorsViweSet(viewsets.ModelViewSet):
    """Showing all Doctors"""
    
    queryset = Doctor.objects.all();
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'crm']
    
class ScheduleViewSet(viewsets.ModelViewSet):
    """Showing all schedule"""
    
    queryset = Schedule.objects.all().filter(day__gte = datetime.date.today()).order_by('day', 'hour')
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['doctor', 'day', 'hour']
    