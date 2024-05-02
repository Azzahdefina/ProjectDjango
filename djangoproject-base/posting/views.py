from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "posting/index.html")

def about(request):
    return render(request, "posting/about.html")

def category(request):
    return render(request, "posting/category.html")

def myskills(request):
    return render(request, "posting/myskills.html")

