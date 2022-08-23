from dataclasses import field, fields
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):

    class Meta:
        model=Tarea
        fields=['tarea']