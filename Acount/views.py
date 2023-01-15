from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from .Forms import Forms_SingUp

from .models import Utilisateur2

from django.http import HttpResponse

from django.contrib import messages


import json

from .auth import CustomAuthBackend

# Create your views here.
def login(request):
    if request.session.get('Login') != 'true':
      if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = CustomAuthBackend.authenticate(request, username=username, password=password)
        if user is not None:
            request.session['Login'] = 'true'
            return redirect('/', )
            #return render(request, 'bootleaf-master/index.html', {'login':request.session.get('Login')})

        else:
            # Return an 'invalid login' error message.
            print("inv")
            messages.error(request, 'Form submission not successful')
            return redirect('/acount/login', )
      else:
        # Render the login template
        print("the login")
        #messages.success(request, 'Form submission not successful')
        #return redirect('/', )
        return render(request, 'LogIn.html', )
    else:
      return redirect('/', )



def signup(request):
    if request.session.get('Login') != 'true':
      
      if request.method == 'POST':
          form = Forms_SingUp.SignUpForm(request.POST)
          if form.is_valid():
              if form.cleaned_data['Password'] != form.cleaned_data['confirm_password']:
                  form.add_error('confirm_password', 'Passwords do not match')
              else:
                  messages.success(request, 'Form submission successful')
                  form.save()
                  return redirect('/acount/login',)
      else:
          form = Forms_SingUp.SignUpForm()
      
      return render(request, 'SingUp.html', {'form': form,})
    else:
      return redirect('/', )


def Lougout(request):
  request.session['Login'] = "false"
  print(request.session.get('Login'))
  return redirect('/acount/login',)


def profile(request):
  return render(request,"profile.html")

def update(request,id):
  if request.session.get('Login') == 'true':
    my_model_instance = Utilisateur2.objects.get(id=id)
    if request.method == 'POST':
        my_model_instance.Real_name = request.POST.get('Real_name',my_model_instance.Real_name)
        my_model_instance.Email = request.POST.get('Email',my_model_instance.Email)
        if request.POST.get('Type_counte') == 'on':
          my_model_instance.Type_counte = True
        else:
          my_model_instance.Type_counte=False
        #my_model_instance.Password = request.POST.get('Password',my_model_instance.Password)
        if request.POST.get('Password') == "":
          my_model_instance.Password = request.POST.get('Password',my_model_instance.Password)
        else:
          if request.POST.get('Password') == request.POST.get('ConfPassword'):
            my_model_instance.Password = request.POST.get('Password',my_model_instance.Password)
          else:
            my_model_instance.add_error('ConfPassword', 'Passwords do not match')
        my_model_instance.save()
        return redirect('/')
    return render(request, 'profile.html', {'object': my_model_instance})
  else:
    return redirect('/', )
