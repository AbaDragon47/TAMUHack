from django.shortcuts import render

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request,'myclasses/index.html', {'title':'Home'})