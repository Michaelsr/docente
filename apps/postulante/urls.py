from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.postulante.views import PostulanteCreate, PostulanteList, PostulanteUpdate, PostulanteDelete
from django.urls import path

urlpatterns = [
    url(r'^nuevopostulante/$', login_required(PostulanteCreate.as_view()), name='crearPostulante'),
    url(r'^listapostulante/$', login_required(PostulanteList.as_view()), name='listarPostulante'),
    url(r'^edidpostulante/(?P<pk>\d+)/$', login_required(PostulanteUpdate.as_view()), name='editarPostulante'),
    url(r'^deletepostulante/(?P<pk>\d+)/$', login_required(PostulanteDelete.as_view()), name='eliminarPostulante'),
]