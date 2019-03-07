from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'InheritanceApp/index.html')


def comments(request):
    return render(request, 'InheritanceApp/comments.html')


def poster(request):
    return render(request, 'InheritanceApp/poster.html')


def details(request):
    return render(request, 'InheritanceApp/details.html')
