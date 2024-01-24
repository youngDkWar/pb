from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import CRUD


@api_view(['POST'])
def create_field_api(request):
    return Response(data=CRUD.create_field(request), status=200)


@api_view(['GET'])
def create_field_api(request):
    return Response(data=CRUD.create_field(request), status=200)


@api_view(['POST'])
def create_agents_api(request):
    return Response(data=CRUD.create_agent(request), status=200)