from django.shortcuts import render, redirect
from .forms import CarModel, CarForm


# Create your views here.
def index(request):
    return render(request, 'InheritanceApp/movie/index.html')


def comments(request):
    return render(request, 'InheritanceApp/movie/comments.html')


def poster(request):
    return render(request, 'InheritanceApp/movie/poster.html')


def details(request):
    return render(request, 'InheritanceApp/movie/details.html')


def home(request):
    return render(request, 'InheritanceApp/carDealer/index.html')


def sell(request):
    form = CarForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("list")
    return render(request, 'InheritanceApp/carDealer/sell.html', {"form":form})


def list(request):
    return render(request, 'InheritanceApp/carDealer/list.html', {"allCars": CarModel.objects.all()})


def team(request):
    return render(request, 'InheritanceApp/carDealer/team.html')
