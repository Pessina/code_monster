from django.urls import path

from . import views

urlpatterns = [
    path('pub/<str:topic>/<str:payload>', views.pub, name='pub'),
    path('', views.index, name='index')
]
