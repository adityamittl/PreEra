from django.shortcuts import render

# Create your views here.


def dianos(request):
    return render(request, 'dinosaurs.html')


def stoneage(request):
    return render(request, 'stoneAgeTools.html')

def homepage(request):
    return render(request, 'home.html')

def maps(request):
    return render(request,'map.html')


def tour(request):
    return render(request,'tour.html')

