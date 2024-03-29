from django.urls import path

from . import views, api

api_path = "api"

urlpatterns = [
    path("", views.index, name="index"),
    path(f'{api_path}/create/field', api.create_field_api),
    path(f'{api_path}/create/agent', api.create_agents_api),
    path(f'{api_path}/create/field-rule', api.create_field_rules_api),
    path(f'{api_path}/create/agent-rule', api.create_agent_rules_api),

    path(f'{api_path}/get/field', api.get_field_api),
    path(f'{api_path}/get/agent', api.get_agent_api),
    path(f'{api_path}/get/field-rule', api.get_field_rules_api),
    path(f'{api_path}/get/agent-rule', api.get_agent_rules_api),

    path(f'{api_path}/patch/field', api.patch_field_api),
    path(f'{api_path}/patch/agent', api.patch_agent_api),
    path(f'{api_path}/patch/field-rule', api.patch_field_rules_api),
    path(f'{api_path}/patch/agent-rule', api.patch_agent_rules_api),

    path(f'{api_path}/delete/field', api.delete_field_api),
    path(f'{api_path}/delete/agent', api.delete_agent_api),
    path(f'{api_path}/delete/field-rule', api.delete_field_rules_api),
    path(f'{api_path}/delete/agent-rule', api.delete_agent_rules_api),
]