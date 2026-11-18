from django import forms
from . models import Crackers

class CrackerForm(forms.ModelForm):
    class Meta:
        model = Crackers
        fields = "__all__"