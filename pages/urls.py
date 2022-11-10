from django.urls import path
from .views import homePegeView

urlpatterns = [
    path('',homePegeView,name='home')
]
