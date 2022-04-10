"""H&W Airlines."""

from django.shortcuts import render
from django.http import HttpResponse

"""Views page for the airline application."""


def home(request):
    """Home page function."""
    return render(request, 'airline/home.html')


def about():
    """About page function."""
    return HttpResponse()