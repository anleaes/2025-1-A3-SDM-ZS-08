from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tecnicoEspecialidade'

router = routers.DefaultRouter()
router.register('', views.TecnicoEspecialidadeViewSet, basename='tecnicoEspecialidade')

urlpatterns = [
    path('', include(router.urls) )
]