from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.evaluadores.views import EvaluadoresCreate, EvaluadoresDelete, EvaluadoresUpdate, EvaluadoresList
from django.urls import path

urlpatterns = [
    url(r'^nuevoevaluador/$', login_required(EvaluadoresCreate.as_view()), name='crearevaluadores'),
    url(r'^listaevaluador/$', login_required(EvaluadoresList.as_view()), name='listarevaluadores'),
    url(r'^edidevaluador/(?P<pk>\d+)/$', login_required(EvaluadoresUpdate.as_view()), name='editarevaluadores'),
    url(r'^deleteevaluador/(?P<pk>\d+)/$', login_required(EvaluadoresDelete.as_view()), name='eliminarevaluadores'),
]