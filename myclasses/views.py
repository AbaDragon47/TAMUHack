from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from users.models import Syllabus
from .forms import UploadSyllabusForm
import os
from django.conf import settings
# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES.getlist('syllabus') and request.POST.get('title'):
        # Iterate through the list of uploaded files
        for syllabus_file in request.FILES.getlist('syllabus'):
            syllabus = Syllabus.objects.create(
                user=request.user,  # Link syllabus to logged-in user
                title=request.POST['title'],  # Use file name for the class name or generate dynamically
                syllabus=syllabus_file
            )

            syllabus.save()  # Save each uploaded syllabus

        # After upload, re-render the homepage with the updated syllabi
    classes = Syllabus.objects.all()
    return render(request, 'myclasses/index.html', {'title': 'Home', 'classes': classes})

def myClasses(request):
    return render(request,'study/class.html',{'title':'Classes'})

def upload(request):
    return render(request,'myclasses/upload_page.html',{'title':'Upload'})

def login(request):
    return render(request,'users/login.html',{'title':'Login'})
  
def performance(request):
    return render(request, 'performance/perf.html',{'title':'Performance'})

def class_detail(request, title):
    # Fetch the syllabus object based on the title
    syllabus = get_object_or_404(Syllabus, title=title)

    # Dummy notes and topics (you can replace these with database data)
    notes = "This is a note for " + title
    topics = "1, 2, 3"

    # Render a template for the class detail
    return render(request, 'study/class.html', {
        'syllabus': syllabus,
        'notes': notes,
        'topics': topics
    })

def assessment(request):
    return render(request, 'myclasses/assessment.html',{'title':'Assessment'})