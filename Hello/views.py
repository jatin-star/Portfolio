from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def Hello(request):
    return HttpResponse("Hello world!")


def portfolio_page(request):
    return render(request, "index.html")


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        send_mail(
            'Contact Info',  # Subject
            f'Name: {name}\nEmail: {email}\nMessage: {message}',  # Message
            settings.EMAIL_HOST_USER,  # Sender email
            ['himanshuprajapati@usf.edu'],  # Recipient email(s)
            fail_silently=False,  # Set to True to ignore errors
        )

        return render(request, 'mail.html')
