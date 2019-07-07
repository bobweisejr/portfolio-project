from django.shortcuts import render

from .models import Job


def home1(request):
    jobs = Job.objects
    return render(request, 'jobs/home1.html', {'jobs':jobs})
