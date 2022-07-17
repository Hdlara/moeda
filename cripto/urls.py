# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from .api.views import ConsultaPeriodoListAPIView

urlpatterns = [
   path(
      'consulta/<str:moeda>/<str:init>/<str:end>',
      ConsultaPeriodoListAPIView.as_view(),
      name='consulta-eriodo'
   ),

   path('', views.generate_chart, name='generate_chart'),
]