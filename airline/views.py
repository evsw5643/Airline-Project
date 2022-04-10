"""H&W Airlines."""

from django.shortcuts import render
from django.http import HttpResponse
from requests import request
"""Views page for the airline application."""


def home():
    """Home page function."""
    return render(request, 'airline/main.html')


def about():
    """About page function."""
    return HttpResponse()