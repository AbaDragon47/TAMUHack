from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import Syllabus
from .forms import UploadSyllabusForm

# Create your views here.
def home(request):
    classes = Syllabus.objects.all()
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
        return render(request, 'myclasses/index.html', {'classes': classes})

    classes = Syllabus.objects.all()
    return render(request,'myclasses/index.html', {'title':'Home','classes': classes})

def myClasses(request):
    return render(request,'study/class.html',{'title':'Classes'})

def upload(request):
    return render(request,'myclasses/upload_page.html',{'title':'Upload'})
