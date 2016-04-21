from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import UserCreateForm

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', {'form': form})