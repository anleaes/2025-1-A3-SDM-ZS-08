from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'endereco'

router = routers.DefaultRouter()
router.register('', views.EnderecoViewSet, basename='endereco')

urlpatterns = [
    path('', include(router.urls) )
]