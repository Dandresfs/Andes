from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from region import views

urlpatterns = [
    url(r'^$', login_required(views.InicioView.as_view()),name="region"),
    url(r'^(?P<pk>\w+)/$', login_required(views.RegionView.as_view()),name="region_rol"),
    url(r'^(?P<pk>\w+)/cpe/$', login_required(views.CpeView.as_view())),

    url(r'^(?P<pk>\w+)/cpe/formacion/$', login_required(views.CpeFormacionView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/funcionarios/(?P<eje>\w+)/$', login_required(views.CpeFuncionarioView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/formadores/$', login_required(views.CpeFormadorView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/formadores/(?P<tipo>\w+)/$', login_required(views.CpeFormadorTipoView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/formacion/etic@/', include('diplomado.urls')),
    url(r'^(?P<pk>\w+)/cpe/formacion/funcionarios/(?P<eje>\w+)/hv/$', login_required(views.hvFuncionarios)),
    url(r'^(?P<pk>\w+)/cpe/formacion/funcionarios/(?P<eje>\w+)/contratos/$', login_required(views.contratosFuncionarios)),

    url(r'^(?P<pk>\w+)/cpe/formacion/formadores/(?P<tipo>\w+)/hv/$', login_required(views.hv)),
    url(r'^(?P<pk>\w+)/cpe/formacion/formadores/(?P<tipo>\w+)/contratos/$', login_required(views.contratos)),
    url(r'^(?P<pk>\w+)/cpe/formacion/formadores/(?P<tipo>\w+)/ruteo/$', login_required(views.ruteo)),

    url(r'^(?P<pk>\w+)/cpe/acceso/$', login_required(views.CpeAccesoView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/acceso/funcionarios/(?P<eje>\w+)/$', login_required(views.CpeFuncionarioView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/acceso/funcionarios/(?P<eje>\w+)/hv/$', login_required(views.hvFuncionarios)),
    url(r'^(?P<pk>\w+)/cpe/acceso/funcionarios/(?P<eje>\w+)/contratos/$', login_required(views.contratosFuncionarios)),

    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/territoriales/$', login_required(views.CpeGestorView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/territoriales/hv/(?P<tipo>\w+)/$', login_required(views.hvGestores)),
    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/territoriales/contratos/(?P<tipo>\w+)/$', login_required(views.contratosGestores)),
    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/territoriales/ruteo/(?P<tipo>\w+)/$', login_required(views.ruteoGestores)),

    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/apoyo/$', login_required(views.CpeGestorApoyoView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/apoyo/hv/(?P<tipo>\w+)/$', login_required(views.hvGestores)),
    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/apoyo/contratos/(?P<tipo>\w+)/$', login_required(views.contratosGestores)),
    url(r'^(?P<pk>\w+)/cpe/acceso/gestores/apoyo/ruteo/(?P<tipo>\w+)/$', login_required(views.ruteoGestoresApoyo)),


    url(r'^(?P<pk>\w+)/cpe/administrativo/$', login_required(views.CpeAdministrativoView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/administrativo/informes/$', login_required(views.CpeAdministrativoInformesView.as_view())),
    url(r'^(?P<pk>\w+)/cpe/administrativo/obligaciones/$', login_required(views.CpeAdministrativoObligacionesView.as_view())),

    url(r'^(?P<pk>\w+)/andes/$', login_required(views.AndesView.as_view()),name="andes_rol"),
    url(r'^(?P<pk>\w+)/andes/administrativo/', include('administrativo.urls')),
    url(r'^(?P<pk>\w+)/andes/acceso/', include('acceso.urls')),
    url(r'^(?P<pk>\w+)/andes/financiero/', include('financiero.urls')),
    url(r'^(?P<pk>\w+)/andes/formacion/', include('formacion.urls')),
]