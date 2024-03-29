from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import CRUD


@api_view(['POST'])
def create_field_api(request):
    return Response(data=CRUD.create_field(request), status=200)


@api_view(['GET'])
def get_field_api(request):
    return Response(data=CRUD.get_field(request), status=200)


@api_view(['PATCH'])
def patch_field_api(request):
    return Response(data=CRUD.patch_field(request), status=200)


@api_view(['DELETE'])
def delete_field_api(request):
    return Response(data=CRUD.delete_field(request), status=200)


@api_view(['POST'])
def create_agents_api(request):
    return Response(data=CRUD.create_agent(request), status=200)


@api_view(['GET'])
def get_agent_api(request):
    return Response(data=CRUD.get_agent(request), status=200)


@api_view(['PATCH'])
def patch_agent_api(request):
    return Response(data=CRUD.patch_agent(request), status=200)


@api_view(['DELETE'])
def delete_agent_api(request):
    return Response(data=CRUD.delete_agent(request), status=200)


@api_view(['POST'])
def create_field_rules_api(request):
    return Response(data=CRUD.create_field_rules(request), status=200)


@api_view(['GET'])
def get_field_rules_api(request):
    return Response(data=CRUD.get_field_rules(request), status=200)


@api_view(['PATCH'])
def patch_field_rules_api(request):
    return Response(data=CRUD.patch_field_rules(request), status=200)


@api_view(['DELETE'])
def delete_field_rules_api(request):
    return Response(data=CRUD.delete_field_rules(request), status=200)


@api_view(['POST'])
def create_agent_rules_api(request):
    return Response(data=CRUD.create_agent_rules(request), status=200)


@api_view(['GET'])
def get_agent_rules_api(request):
    return Response(data=CRUD.get_agent_rules(request), status=200)


@api_view(['PATCH'])
def patch_agent_rules_api(request):
    return Response(data=CRUD.patch_agent_rules(request), status=200)


@api_view(['DELETE'])
def delete_agent_rules_api(request):
    return Response(data=CRUD.delete_agent_rules(request), status=200)