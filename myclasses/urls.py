from django.urls import path
from . import views

urlpatterns = [
    #when main urls calls, it cuts off what it matched til
    #then sends the rest of the string
    path('', views.home, name='site-home'),
    

]