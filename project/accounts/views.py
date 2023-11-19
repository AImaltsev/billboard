from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib import messages

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm  # Замените на новую форму
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your registration. Please check the form and try again.')
        return super().form_invalid(form)