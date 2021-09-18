from django import forms
from .models import ProductReport


class ProdutcReportForm(forms.ModelForm):
    class Meta:
        model = ProductReport
        fields = ('image', )
