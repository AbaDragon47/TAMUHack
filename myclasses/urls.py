from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='site-home'),
    path('classes/', views.myClasses, name='myClasses'),
    path('upload/', views.upload, name='upload'),
    path('login/' , views.login, name='login'),
    path('performance/', views.performance, name="performance")

]