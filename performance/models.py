# performance/models.py
from django.db import models
from django.contrib.auth.models import User

class StudyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)  # Subject or topic being studied
    study_time = models.IntegerField()  # Time spent studying (in minutes)
    timestamp = models.DateTimeField(auto_now_add=True)  # When the study session occurred

    def __str__(self):
        return f'{self.user.username} studied {self.subject} for {self.study_time} minutes'

class Badge(models.Model):
    name = models.CharField(max_length=100)  # Name of the badge
    description = models.TextField()  # Description of how to earn the badge
    image = models.ImageField(upload_to='badges/', null=True, blank=True)  # Badge image (optional)

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} earned {self.badge.name}'

class UserPerformance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_study_time = models.IntegerField(default=0)  # Total time spent studying (in minutes)
    total_badges = models.IntegerField(default=0)  # Total number of badges earned

    def __str__(self):
        return f'{self.user.username} Performance'
