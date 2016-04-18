from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def index(request):
    user_list = Profile.objects.all()
    context = {'user_list': user_list}
    return render(request, 'connect/index.html', context)
    
def detail(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist!")
    return render(request, 'connect/detail.html', {'profile': profile})

def messages(request, profile_id):
    response = "You're looking at messages of profile %s."
    return HttpResponse(response % profile_id)