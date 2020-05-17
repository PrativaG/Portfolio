from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def skills(request):
    return render(request, "skills.html")

def experience(request):
    return render(request, "experience.html")

def projects(request):
    return render(request, "projects.html")