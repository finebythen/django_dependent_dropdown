from django.urls import path

from . import views

urlpatterns = [
    # --> View
    path('', views.person_create_view, name='person_add'),

    # --> Ajax
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
