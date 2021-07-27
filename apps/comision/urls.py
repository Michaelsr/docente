from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.comision.views import ComisionList, ComisionCreate, ClienteDelete, ClienteUpdate
from django.urls import path

urlpatterns = [
    url(r'^nuevacomisione/$', login_required(ComisionCreate.as_view()), name='crearComision'),
    url(r'^listacomision/$', login_required(ComisionList.as_view()), name='listarComision'),
    url(r'^edidcomision/(?P<pk>\d+)/$', login_required(ClienteUpdate.as_view()), name='editarComision'),
    url(r'^deletecomisio/(?P<pk>\d+)/$', login_required(ClienteDelete.as_view()), name='eliminarComision'),
]