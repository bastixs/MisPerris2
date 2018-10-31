from django.urls import path, re_path, include
from .views import SignUpView, BienvenidaView, SignInView, SignOutView
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^$', views.base),
    re_path(r'^perro/listar/$', views.perro_list),
    path('perro/detalle/<int:pk>', views.perro_detalle, name='detalle'),
    re_path(r'^perro/eliminar/(?P<pk>[0-9]+)/$', views.perro_eliminar, ''),
    re_path(r'^perro/editar/(?P<pk>[0-9]+)/$', views.perro_editar, ''),
    re_path(r'^perro/nuevo/$', views.perro_nuevo, ''),
    re_path(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    re_path(r'^bienvenida/$', BienvenidaView.as_view(), name='bienvenida'),
    re_path(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    re_path(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    re_path(r'^usuarios/$', views.usuarios, name='usuarios'),
]
