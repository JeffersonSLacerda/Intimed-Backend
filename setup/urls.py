from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from medicar.views import DoctorsViweSet, ScheduleViewSet

router = routers.DefaultRouter()
router.register('medico', DoctorsViweSet, basename='Medicos')
router.register('consultas', ScheduleViewSet, basename='Consultas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
