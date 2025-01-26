from django.shortcuts import render

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request,'myclasses/index.html', {'title':'Home'})

def myClasses(request):
    return render(request,'study/class.html',{'title':'Classes'})

def upload(request):
    return render(request,'myclasses/upload_page.html',{'title':'Upload'})

def login(request):
    return render(request,'users/login.html',{'title':'Login'})
  
def performance(request):
    return render(request, 'performance/perf.html',{'title':'Performance'})
