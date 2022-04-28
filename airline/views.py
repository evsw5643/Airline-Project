"""H&W Airlines."""

from curses.ascii import CR

import airline
from .forms import ReadFileForm, LoginForm, RegisterForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import CreateView, FormView
from .models import Airplane
#class based views

User = get_user_model()
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

def home(request):
    airplane = Airplane.objects.get(pk = 1)
    destination = airplane.airplane_destination
    date = airplane.airplane_date_of_departure
    context = {
        'airplane': airplane,
        'destination': destination,
        'date': date,
    }
    return render(request, 'airline/home.html', context=context)

class LoginView(FormView):
    form_class = LoginForm
    template_name = "airline/login.html"
    success_url = "home.html"

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/home.html")
        return super(LoginView, self).form_invalid(form)


# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             try:
#                 del request.session['guest_email_id']
#             except:
#                 pass
#             if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/")
#         else:
#             # Return an 'invalid login' error message.
#             print("Error")
#     return render(request, "airline/login.html", context)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'airline/register.html'
    success_url = '/home.html'


class AboutView(CreateView):
    form_class = RegisterForm
    template_name = 'airline/about.html'
    success_url = '/about.html'


class FlightsView(CreateView):
    form_class = RegisterForm
    template_name = 'airline/flights.html'
    success_url = '/flights.html'


class BookingView(CreateView):
    form_class = RegisterForm
    template_name = 'airline/booking.html'
    success_url = '/checkout.html'


class CheckoutView(CreateView):
    form_class = RegisterForm
    template_name = 'airline/checkout.html'
    success_url = '/confirmation.html'


class ConfirmationView(CreateView):
    form_class = RegisterForm
    template_name = 'airline/confirmation.html'
    success_url = '/confirmation.html'

# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         form.save()
#     return render(request, "airline/register.html", context)