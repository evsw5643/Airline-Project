"""airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views
from .views import LoginView, RegisterView, AboutView, FlightsView, CheckoutView, ConfirmationView
import airline

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home.html', views.home, name='home'),
    path('', LoginView.as_view()),#goes to login page first
    path('register.html', RegisterView.as_view(), name = "Register"),
    path('login.html', LoginView.as_view(), name = "Login"), #goes to login page first
    path('about.html', AboutView.as_view(), name = "About"),#goes to login page first
    path('flights.html', FlightsView.as_view(), name = "Flights"),#goes to login page first
    path('booking.html/<airplane_name>/', views.booking, name = "booking"),#goes to login page first

    path('checkout.html', CheckoutView.as_view(), name = "Checkout"),#goes to login page first
    path('confirmation.html', ConfirmationView.as_view(), name = "Confirmation"),#goes to login page first


    # ex: /polls/5/
]
