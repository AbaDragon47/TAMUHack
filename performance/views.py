# performance/views.py
from django.shortcuts import render
from .models import StudyLog, UserBadge, UserPerformance
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user

    try:
        performance = UserPerformance.objects.get(user=user)
    except UserPerformance.DoesNotExist:
        # If performance doesn't exist, create it
        performance = UserPerformance.objects.create(user=user)
    # Get the user's study logs
    study_logs = StudyLog.objects.filter(user=user).order_by('-timestamp')[:5]  # Most recent 5 logs

    # Get the badges earned by the user
    badges = UserBadge.objects.filter(user=user)

    # Get the user's performance metrics
    performance = UserPerformance.objects.get(user=user)

    # Total study time
    total_study_time = sum(log.study_time for log in study_logs)

    context = {
        'user':user,
        'study_logs': study_logs,
        'badges': badges,
        'performance': performance,
        'total_study_time': total_study_time,
    }
    return render(request, 'performance/perf.html', context)
