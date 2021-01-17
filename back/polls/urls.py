from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
	path('final/', views.final),
	path('getTabla/', views.getTabla),
]