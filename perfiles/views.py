from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from app_creditos.models import Clientes
from django.contrib.auth.mixins import LoginRequiredMixin

from perfiles.forms import UserRegisterForm, UserUpdateForm
from django.views.generic import UpdateView



def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save() 

            nombre = formulario.cleaned_data.get('first_name')
            apellido = formulario.cleaned_data.get('last_name')
            dni = formulario.cleaned_data.get('dni')
            email = formulario.cleaned_data.get('email')
            cliente = Clientes(user=usuario, nombre=nombre, apellido=apellido, dni=dni, email=email)
            cliente.save()
         
            login(request, usuario)
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='perfiles/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='perfiles/login.html',
        context={'form': form},
    )

class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'perfiles/formulario_perfil.html'

   def get_object(self, queryset=None):
       return self.request.user
