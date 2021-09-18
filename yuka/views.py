from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView

from .form import ProdutcReportForm
from .models import ProductReport


class TopView(TemplateView):
    template_name = 'top.html'


class HSVReportDetailView(DetailView):
    model = ProductReport
    template_name = "HSVreportDetailView.html"


class HSVReportCreateView(CreateView):
    model = ProductReport
    template_name = 'HSVreportCreate.html'
    form_class = ProdutcReportForm
    success_url = "/yuka"
