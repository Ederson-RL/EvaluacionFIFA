from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


class HomeView(TemplateView):
    template_name = 'home.html'


class loginView(AuthLoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        # Redirige al panel de administración
        return reverse_lazy('admin:index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Cambia 'home' por la URL a la que quieres redirigir después del registro
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
