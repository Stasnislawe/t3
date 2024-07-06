from django.urls import path, include
from .views import minavgmaxconc, HomeView
from rest_framework import routers
from .views import MineralViewSet, download_model

router = routers.DefaultRouter()
router.register(r'mineral', MineralViewSet)


urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('minavgmax/<int:pk>', minavgmaxconc, name='minavgmax'),
    path('', include(router.urls)),
    path('upload/', download_model, name='upload'),
]