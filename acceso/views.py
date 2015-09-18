from django.views.generic import TemplateView
from mixins.mixins import AccesoMixin
from region.models import Region
from gestor.models import Gestor
from radicado.models import Radicado
import datetime

from .models import Evidencia
from rest_framework import mixins
from rest_framework import generics
from .serializers import EvidenciaSerializer
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext

class EvidenciaViewSet(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer
    lookup_url_kwarg = 'id_evidencia'


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class AccesoView(AccesoMixin,TemplateView):
    template_name = 'acceso.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        return super(AccesoView,self).get_context_data(**kwargs)

class AccesoCalificacionView(AccesoMixin,TemplateView):
    template_name = 'acceso_gestores.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        return super(AccesoCalificacionView,self).get_context_data(**kwargs)

class AccesoListadoRadicadosView(AccesoMixin,TemplateView):
    template_name = 'acceso_radicados.html'

    def get_context_data(self, **kwargs):
        kwargs['REGION'] = Region.objects.get(pk=self.kwargs['pk']).nombre
        kwargs['NOMBRE'] = Gestor.objects.get(pk=self.kwargs['id_gestor']).nombre
        kwargs['ID_REGION'] = self.kwargs['pk']
        kwargs['ID_GESTOR'] = self.kwargs['id_gestor']
        return super(AccesoListadoRadicadosView,self).get_context_data(**kwargs)

def evidencia_form(request,id_radicado,pk,id_gestor):
    EvidenciaFormSet = modelformset_factory(Evidencia, fields=('soporte',),extra=0)
    if request.method == "POST":
        formset = EvidenciaFormSet(request.POST, request.FILES, queryset=Evidencia.objects.filter(radicado__id=id_radicado).filter(corte=None))
        if formset.is_valid():
            formset.save()
            for form in formset.forms:
                if form.cleaned_data['soporte'] != None:
                    obj = Evidencia.objects.get(pk=form.instance.id)
                    obj.usuario = request.user
                    obj.modificacion = datetime.datetime.now()
                    obj.save()
    else:
        formset = EvidenciaFormSet(queryset=Evidencia.objects.filter(radicado__id=id_radicado).filter(corte=None),)
    return render_to_response("evidencias_radicado.html",{"formset":formset,"user":request.user,"REGION":Region.objects.get(pk=pk).nombre,
                                                          "gestor":Gestor.objects.get(pk=id_gestor).nombre,"radicado":Radicado.objects.get(pk=id_radicado)},
                              context_instance=RequestContext(request))