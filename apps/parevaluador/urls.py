from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.parevaluador.views import ParevaCreate, ParevaDelete, ParevaList, ParevaUpdate
from django.urls import path

urlpatterns = [
    url(r'^Nuevoparevaluador/$', login_required(ParevaCreate.as_view()), name='crearparevaluador'),
    url(r'^Listaparevaluador/$', login_required(ParevaList.as_view()), name='listarparevaluador'),
    url(r'^Editarparevaluador/(?P<pk>\d+)/$', login_required(ParevaUpdate.as_view()), name='editarparevaluador'),
    url(r'^Eliminarparevaluador/(?P<pk>\d+)/$', login_required(ParevaDelete.as_view()), name='eliminarparevaluador'),
]
