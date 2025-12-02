from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse


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

def team(request):
    return render(request,'stay/team.html')

def login(request):
    return render(request, 'stay/login.html')


def submit_contact_query(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '')
        query = request.POST.get('message', '')

        print(f"Received data: first_name={first_name}, last_name={last_name}, email={email}, subject={subject}, query={query}")

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            query=query
        )

        contact.save()

        return JsonResponse({'success': True, 'message': 'Your message has been submitted successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

