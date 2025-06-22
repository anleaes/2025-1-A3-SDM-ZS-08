from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'notificacao'

router = routers.DefaultRouter()
router.register('', views.NotificacaoViewSet, basename='notificacao')

urlpatterns = [
    path('', include(router.urls) )
]