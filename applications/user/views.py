from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import RegistrationForm


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register_page.html'
    success_url = reverse_lazy('home-page')