from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request ,"core/index.html")



def about(request):
    return render(request ,"core/about.html")


def contact(request):
    return render(request ,"core/contact.html")


def review(request):
    return render(request ,"core/review.html")


def store(request):
    return render(request ,"core/store.html")



