from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.contrib.auth import login, authenticate

def index(request):
    context = {'user':request.user}
    return render(request, 'accounts/index.html', context)

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('accounts:index')
    else:
        form = MyUserCreationForm()
    
    context = {'form':form}
    return render(request, 'accounts/register.html', context)