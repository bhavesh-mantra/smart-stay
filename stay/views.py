from django.shortcuts import render

def home(request):
    return render(request,'stay/index.html')

def contact(request):
    return render(request,'stay/contact.html')

def about(request):
    return render(request,'stay/about.html')

def service(request):
    return render(request,'stay/service.html')

def project(request):
    return render(request,'stay/project.html')

def feature(request):
    return render(request,'stay/feature.html')
