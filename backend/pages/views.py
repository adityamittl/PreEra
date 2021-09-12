from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dianos(request):
    return render(request, 'dinosaurs.html')

@login_required
def stoneage(request):
    return render(request, 'stoneAgeTools.html')
def homepage(request):
    return render(request, 'home.html')
@login_required
def maps(request):
    return render(request,'map.html')

@login_required
def tour(request):
    return render(request,'tour.html')

