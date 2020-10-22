from django.urls import path
from django.conf.urls import url
from . import views

#urlpatterns = [
    #path('', views.home, name='home'),
    #path('cal1', views.cal1, name='cal1'),

#]

urlpatterns = [
    url(r'^$', views.index),
    url(r'^history/', views.history),
    url(r'^equate', views.equate)
]
