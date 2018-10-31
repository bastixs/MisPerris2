
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import time
from django.contrib.auth.models import User
from .models import Dueño, Mascota, Perfil
from .forms import Mascotaform, SignUpForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class SignOutView(LogoutView):
    pass


class SignInView(LoginView):
    template_name = 'iniciar_sesion.html'


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/bienvenida')


class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'


def usuarios(request):
    usuarios = User.objects.all()
    mascotas = Mascota.objects.all()
    context = {'mascotas': mascotas, 'usuarios': usuarios}
    return render(request, 'recetea_usuarios.html', context)


def index(request):
    return render(request, 'index.html')


def base(request):
    a = time.strftime("%c")
    return render(request, 'base.html',  {'fechaHora': a})


def perro_list(request):
    mascotas = Mascota.objects.all()
    return render(request, 'listar_perro.html', {'Mascota': mascotas})


def perro_detalle(request, pk):
    mascotas = get_object_or_404(Mascota, pk=pk)
    return render(request, 'detalle_perro.html', {'Mascota': mascotas})


def perro_eliminar(request, pk):

    Mascota.objects.filter(pk=pk).delete()
    mascotas = Mascota.objects.all()
    return render(request, 'listar_perro.html', {'Mascota': mascotas})


def perro_editar(request, pk):
    mascotas = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        form = Mascotaform(request.POST, instance=mascotas)
        if form.is_valid():
            mascotas = form.save(commit=False)
            mascotas.save()
            return redirect('detalle', pk=mascotas.pk)
    else:
        form = Mascotaform(instance=mascotas)
        return render(request, 'editar_perro.html', {'form': form})


def perro_nuevo(request):
    if request.method == "POST":
        form = Mascotaform(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.save()
            return redirect('detalle', pk=mascota.pk)
    else:
        form = Mascotaform()
        return render(request, 'editar_perro.html', {'form': form})
