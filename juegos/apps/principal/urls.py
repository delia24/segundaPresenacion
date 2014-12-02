from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings
urlpatterns = patterns('',
	url(r'^$',inicio),
	
	url(r'^regisusuario/$',nuevoUsuario),
	url(r'^ingresar/$',ingresar),
    url(r'^active/$',user_active_view),
    url(r'^perfil/$',perfil),
    url(r'^lista/$',inicio_view),




    url(r'^tema/$',registro_tema, name='Tema'),
    url(r'^tema/add/(\d+)/$',add_pregunta, name='agregar_pregunta'),
    url(r'^tema/edit/(\d+)/$',ver_preguntas, name='edit_pregunta'),
    url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='edit_pregunta'),
    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
    #url(r'^registro/pregunta/$',registro_pregunta, name='Pregunta'),
    url(r'^agregar/',agregar, name='agregar_pregunta'),
)

#http://localhost:8001/




