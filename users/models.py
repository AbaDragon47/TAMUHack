from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
# Create your models here.


class LearningProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    learning_style_choices = [
        ('visual', 'Visual'),
        ('auditory', 'Auditory'),
        ('kinesthetic', 'Kinesthetic'),
    ]
    learning_style = models.CharField(max_length=20, choices=learning_style_choices)
    

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    note = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.title

class Syllabus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    syllabus = models.FileField(upload_to='syllabuses/')
    content = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def getTitle(title):
        return os.path.join(settings.BASE_DIR, f"study/templates/study/class_{title}.html")
    
    #move this
    
    

'''class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    pomodoro_sessions = models.IntegerField()  # Count of pomodoro intervals completed
    notes_reviewed = models.ManyToManyField(Note, related_name='study_sessions')

    def __str__(self):
        return f"Study session for {self.user.username} at {self.start_time}"
    '''