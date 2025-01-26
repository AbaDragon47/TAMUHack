from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.
def register(request):
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               #flash message is one time thing
               messages.success(request,f'Account created for {username}, now login!')
               return redirect('login')
          else:
               form = UserRegisterForm()

     else:
          #user creation alredy exists in django
          form = UserRegisterForm()
     return render(request,'users/register.html',{'form':form})


@login_required
def user_logout(request):
     logout(request)
     return render(request, 'users/logout.html')