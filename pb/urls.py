from django.urls import path

from . import views, api

api_path = "api"

urlpatterns = [
    path("", views.index, name="index"),
    path(f'{api_path}/field', api.create_field_api),
    path(f'{api_path}/agent', api.create_agents_api),
]