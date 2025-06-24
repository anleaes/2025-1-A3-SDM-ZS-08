from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tecnico'

router = routers.DefaultRouter()
router.register('', views.TecnicoViewSet, basename='tecnico')

urlpatterns = [
    path('', include(router.urls) )
]