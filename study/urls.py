from django.urls import path, include
from . import views
from myclasses import views as v

urlpatterns = [
    path('', v.class_detail, name='detail'),
    path('notes/<int:syllabus_id>/', views.notes_view, name='notes')
    
]

#gemini, look up LLMs