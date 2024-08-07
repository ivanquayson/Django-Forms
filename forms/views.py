from django.shortcuts import render
from .form import InputForm


def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, 'home.html', context)