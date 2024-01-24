import pytz
from datetime import datetime, timedelta, timezone

from .models import *


def create_field(request):
    """
    :param request: {}
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    fields = Field.objects.all()
    response["fields"] = []
    for e in fields:
        response["fields"].append(
            {
                "name": e.name,
                "create_dt": e.create_dt,
                "author": e.author
            }
        )
    response = {"status": "ok"}
    return response


def create_agent(request):
    """
    :param request:
        {
            "field": <field_id>,
            "agents":
            [
                {
                    "name": "test2",
                    "author": "Kirill"
                },
                {
                    "name": "test2",
                    "author": "Kirill"
                }
            ]
        }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    utc = pytz.UTC
    request_time = (datetime.now()).replace(tzinfo=utc)
    data = request.data
    field_id = data['field']
    field = Field.objects.filter(id=field_id)
    if field:
        f = field.first()
        if data['agents']:
            for e in data['agents']:
                Agent(
                    field=f,
                    name=e['name'],
                    author=e['author'],
                    create_dt=request_time
                ).save()
            response['status'] = "ok"
        else:
            response['status'] = "ERROR: Empty agents"
    else:
        response['status'] = "Field dont exist"
    return response
