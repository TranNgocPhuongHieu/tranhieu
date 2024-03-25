
from django.shortcuts import render
from .models import Experience, Education, Skill

def cv_detail(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    return render(request, 'cvapp/CV1/cv_classic.html', {'experiences': experiences, 'educations': educations, 'skills': skills})
