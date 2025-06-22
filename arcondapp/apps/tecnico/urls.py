app_name = 'cliente'

router = routers.DefaultRouter()
router.register('', views.ClienteViewSet, basename='cliente')

urlpatterns = [
    path('', include(router.urls) )
]