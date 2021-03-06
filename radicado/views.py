from acceso.models import Evidencia, Reasignados, EvidenciaApoyo
from radicado.models import Radicado
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

class RadicadoTableView(BaseDatatableView):
    model = Evidencia
    columns = [
        'radicado',
        'ciclo',
        'componente',
        'id'
    ]

    order_columns = [
        'radicado',
        'radicado',
        'radicado',
        'radicado'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(gestor__id=self.kwargs['id_gestor']).filter(radicado__municipio__id=self.kwargs['id_municipio']).\
            values('radicado__id','radicado__numero','radicado__municipio__nombre',
            'radicado__municipio__departamento__nombre','radicado__zona','radicado__matricula',
            'radicado__nombre_institucion','radicado__dane_institucion','radicado__nombre_sede','radicado__dane_sede').distinct()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__numero__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'radicado':
            return row.radicado.numero
        if column == 'ciclo':
            return str(row.ciclo.nombre)
        if column == 'componente':
            return str(row.componente.nombre)
        else:
            return super(RadicadoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            actividades = Evidencia.objects.all().filter(radicado__id=item['radicado__id'])
            ejecutadas = actividades.exclude(corte=None).count()
            sin_ejecutar = actividades.filter(corte=None).count()
            sin_reportar = actividades.filter(corte=None).exclude(soporte="").count()

            if actividades.count() != 0:
                progreso = format((ejecutadas*100.0)/actividades.count(), '.2f')
            else:
                progreso = 0

            json_data.append([
                item['radicado__id'],
                item['radicado__numero'],
                item['radicado__municipio__nombre'],
                item['radicado__municipio__departamento__nombre'],
                item['radicado__zona'],
                item['radicado__matricula'],
                item['radicado__nombre_institucion'],
                item['radicado__dane_institucion'],
                item['radicado__nombre_sede'],
                item['radicado__dane_sede'],
                ejecutadas,
                sin_ejecutar,
                progreso,
                sin_reportar
            ])
        return json_data

class RadicadoApoyoTableView(BaseDatatableView):
    model = EvidenciaApoyo
    columns = [
        'radicado',
        'ciclo',
        'componente',
        'id'
    ]

    order_columns = [
        'radicado',
        'radicado',
        'radicado',
        'radicado'
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(gestor__id=self.kwargs['id_gestor']).filter(radicado__municipio__id=self.kwargs['id_municipio']).\
            values('radicado__id','radicado__numero','radicado__municipio__nombre',
            'radicado__municipio__departamento__nombre','radicado__zona','radicado__matricula',
            'radicado__nombre_institucion','radicado__dane_institucion','radicado__nombre_sede','radicado__dane_sede').distinct()

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado__numero__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'radicado':
            return row.radicado.numero
        if column == 'ciclo':
            return str(row.ciclo.nombre)
        if column == 'componente':
            return str(row.componente.nombre)
        else:
            return super(RadicadoApoyoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            actividades = EvidenciaApoyo.objects.all().filter(radicado__id=item['radicado__id'])
            ejecutadas = actividades.exclude(corte=None).count()
            sin_ejecutar = actividades.filter(corte=None).count()
            sin_reportar = actividades.filter(corte=None).exclude(soporte="").count()

            if actividades.count() != 0:
                progreso = format((ejecutadas*100.0)/actividades.count(), '.2f')
            else:
                progreso = 0

            json_data.append([
                item['radicado__id'],
                item['radicado__numero'],
                item['radicado__municipio__nombre'],
                item['radicado__municipio__departamento__nombre'],
                item['radicado__zona'],
                item['radicado__matricula'],
                item['radicado__nombre_institucion'],
                item['radicado__dane_institucion'],
                item['radicado__nombre_sede'],
                item['radicado__dane_sede'],
                ejecutadas,
                sin_ejecutar,
                progreso,
                sin_reportar
            ])
        return json_data

class RadicadoTotalTableView(BaseDatatableView):
    max_display_length = 10
    model = Radicado
    columns = [
        'id',
        'numero',
        'municipio',
    ]

    order_columns = [
        'numero',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(region__id=self.kwargs['region'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'numero__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'municipio':
            return str(row.municipio.nombre)
        else:
            return super(RadicadoTotalTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            actividades = Evidencia.objects.filter(radicado__id=item.id)
            ejecutadas = actividades.exclude(corte=None).count()
            sin_ejecutar = actividades.filter(corte=None).count()
            sin_reportar = actividades.filter(corte=None).exclude(soporte="").count()

            if actividades.count() != 0:
                progreso = format((ejecutadas*100.0)/actividades.count(), '.2f')
            else:
                progreso = 0

            json_data.append([
                item.id,
                item.numero,
                item.municipio.nombre,
                item.municipio.departamento.nombre,
                item.zona,
                item.matricula,
                item.nombre_institucion,
                item.dane_institucion,
                item.nombre_sede,
                item.dane_sede,
                ejecutadas,
                sin_ejecutar,
                progreso,
                sin_reportar
            ])
        return json_data

class RadicadoTotalApoyoTableView(BaseDatatableView):
    max_display_length = 10
    model = Radicado
    columns = [
        'id',
        'numero',
        'municipio',
    ]

    order_columns = [
        'numero',
    ]

    def get_initial_queryset(self):
        x = EvidenciaApoyo.objects.all().values_list('radicado__id',flat=True)
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.filter(region__id=self.kwargs['region']).filter(id__in=x)

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'numero__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'municipio':
            return str(row.municipio.nombre)
        else:
            return super(RadicadoTotalApoyoTableView,self).render_column(row,column)

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            actividades = EvidenciaApoyo.objects.filter(radicado__id=item.id)
            ejecutadas = actividades.exclude(corte=None).count()
            sin_ejecutar = actividades.filter(corte=None).count()
            sin_reportar = actividades.filter(corte=None).exclude(soporte="").count()

            if actividades.count() != 0:
                progreso = format((ejecutadas*100.0)/actividades.count(), '.2f')
            else:
                progreso = 0

            json_data.append([
                item.id,
                item.numero,
                item.municipio.nombre,
                item.municipio.departamento.nombre,
                item.zona,
                item.matricula,
                item.nombre_institucion,
                item.dane_institucion,
                item.nombre_sede,
                item.dane_sede,
                ejecutadas,
                sin_ejecutar,
                progreso,
                sin_reportar
            ])
        return json_data

class RadicadoReasignadoView(BaseDatatableView):
    model = Reasignados
    columns = [
        'fecha_reasignado',
        'radicado_origen',
        'radicado_destino',
        'usuario'
    ]

    order_columns = [
        'fecha_reasignado',
    ]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all().filter(region__id=self.kwargs['region'])

    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        q = Q()
        if search:
            q |= Q(**{'radicado_origen__icontains' : search})
            q |= Q(**{'radicado_destino__icontains' : search})
            qs = qs.filter(q)
        return qs

    def render_column(self, row, column):
        if column == 'usuario':
            return str(row.usuario.username)
        else:
            return super(RadicadoReasignadoView,self).render_column(row,column)