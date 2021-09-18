from django.contrib import admin
from django.urls import path, include
from .views import HSVReportCreateView, TopView, HSVReportDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TopView.as_view(), name="top"),
    path('hsv/create/', HSVReportCreateView.as_view(), name='hsv-create'),
    path('hsv/<int:pk>/', HSVReportDetailView.as_view(), name="hsv-detail"),
]
