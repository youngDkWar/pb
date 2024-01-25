from django.urls import path

from . import views, api

api_path = "api"

urlpatterns = [
    path("", views.index, name="index"),
    path(f'{api_path}/create/field', api.create_field_api),
    path(f'{api_path}/get/field', api.get_field_api),
    path(f'{api_path}/create/agent', api.create_agents_api),
    path(f'{api_path}/get/agent', api.get_agent_api),
    path(f'{api_path}/field-rule', api.create_agents_api),
]