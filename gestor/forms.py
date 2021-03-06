from django import forms
from .models import Gestor

class NuevoForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['region','tipo','nombre','cedula','celular','correo','fecha_contratacion']

class GestorFotoForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['foto']

class GestorSoporteForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['hv','certificacion','rut','contrato','contrato_plan_choque','fotocopia_cedula','antecedentes_judiciales','antecedentes_contraloria','liquidacion']

class GestorInformacionForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre','cedula','celular','correo','cargo','profesion','banco','tipo_cuenta','numero_cuenta','eps','pension','arl']

class GestorSeguroForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['seguro_enero','seguro_febrero','seguro_marzo','seguro_abril',
                  'seguro_mayo','seguro_junio','seguro_julio','seguro_agosto',
                  'seguro_septiembre','seguro_octubre','seguro_noviembre','seguro_diciembre',
                  'seguro_enero_1','seguro_febrero_1','seguro_marzo_1','seguro_abril_1',]