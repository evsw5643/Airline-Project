"""H&W Airlines."""

from .forms import ReadFileForm
from django.shortcuts import render
from django.http import HttpResponse

"""Views page for the airline application."""


def home(request):
    """Home page function."""
    return render(request, 'airline/home.html')


def about():
    """About page function."""
    return HttpResponse()

def read_file(request):
    form = ReadFileForm()
    if request.method == 'POST':
        form = ReadFileForm(request.POST, request.FILES)
        if form.is_valid():
            content = request.FILES['file'].read()
    return render(request, 'home.html', locals())
