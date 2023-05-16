from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

from perfiles.forms import UserRegisterForm



def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='perfiles/registro.html',
        context={'form': formulario},
    )

# class RegisterView(View):
#     def get(self, request):
#         form = UserRegisterForm()
#         return render(request, 'perfiles/registro.html', {'form': form})

#     def post(self, request):
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             nombre = form.cleaned_data.get('first_name')
#             apellido = form.cleaned_data.get('last_name')
#             dni = form.cleaned_data.get('dni')
#             email = form.cleaned_data.get('email')
#             cliente = Clientes(user=user, nombre=nombre, apellido=apellido, dni=dni, email=email)
#             cliente.save()

            
#             login(request, user)
#             return redirect('inicio')
#         return render(request, 'inicio', {'form': form})


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
