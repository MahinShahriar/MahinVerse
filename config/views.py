import time

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

import json
from MahinVerse.settings import JSON_FILE

from .models import Project, Blog
from .forms import ContactForm, FormWithCaptcha

with open(JSON_FILE, 'r') as openfile:
    countries = json.load(openfile)


def home_view(request):
    captcha = FormWithCaptcha()
    context = {
        "skills": [
                    {"name": "Python", "logo": "/img/python.png"},
                    {"name": "Django", "logo": "/img/django_logo.png"},
                    {"name": "Django Rest Framework", "logo": "/img/django_rest_logo.png"},
                    {"name": "Flask", "logo": "/img/flask.png"},
                    {"name": "JavaScript", "logo": "/img/js_logo.png"},
                    {"name": "SQL", "logo": "/img/Sql.png"},
                    {"name": "PostgreSQL", "logo": "/img/postgresql.png"},
                    {"name": "MySQL", "logo": "/img/mysql.png"},
                    {"name": "TailwindCSS", "logo": "/img/tw_css.png"},
                    {"name": "HTML 5", "logo": "/img/html.png"},
                    {"name": "CSS", "logo": "/img/css_logo.png"},
                    {"name": "Git", "logo": "/img/git.png"},
                    {"name": "Docker", "logo": "/img/docker.png"},
                    {"name": "Linux(ParrotOS)", "logo": "/img/linux.png"},
                                ],
        "projects": Project.objects.all(),
        "countries": countries,
        "captcha": captcha,
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        captcha = FormWithCaptcha(request.POST)

        if form.is_valid() & captcha.is_valid():
            name = request.POST.get('name')
            email = form.cleaned_data['email']
            try:
                voice_contact = request.POST.get("platform")+' - ' + request.POST.get("country") + request.POST.get("number")
            except TypeError:
                voice_contact = 'N/A'
            subject = 'MahinVerse\t: ' + form.cleaned_data['subject']
            message = form.cleaned_data['message'] + f"\n\nName: {name}\nemail : {email}\n{voice_contact}"

            if request.session.get("last_email") == email:
                messages.warning(request, "You have already sent a message recently. Please wait before sending again.")
                return redirect("/#contact")
            else:

                send_mail(
                            subject,
                            message,
                            email,
                            ['mahinshahriar303@gmail.com'],
                            fail_silently=False,
                        )

                print("\n\n\t\tSuccess !!!!\n\n\n")
                time.sleep(5)
                messages.success(request, f"Thank you {name}, Your message has been sent successfully! You'll be replied via email.")
                request.session["last_email"] = email
                # time.sleep(3)
                return redirect("/")

        elif not captcha.is_valid() :
            messages.error(request, "Captcha field is required !")

        return redirect('/#contact')

    return render(request, 'base.html', context=context)


def blog_view(request):
    context = {
        'posts': Blog.objects.all(),
    }
    return render(request, 'blog.html', context=context)
