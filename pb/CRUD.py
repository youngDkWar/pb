import pytz
from datetime import datetime, timedelta, timezone

from .models import *


def create_field(request):
    """
    :param request:
        {
            "fields":
            [
                {
                    "name": "test1",
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
    if data['fields']:
        for e in data['fields']:
            Field(
                name=e['name'],
                author=e['author'],
                create_dt=request_time
                ).save()
        response['status'] = "ok"
    else:
        response['status'] = "ERROR: Empty fields"
    return response


def patch_field(request):
    """
    :param request:
        {
            "fields":
            [
                {
                    "id": 1,
                    "name": "test1"
                },
                {
                    "id": 2,
                    "name": "test2"
                }
            ]
        }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    data = request.data
    if data['fields']:
        for e in data['fields']:
            field = Field.objects.filter(id=e['id']).first()
            if field:
                field.name = e['name']
                field.save()
            else:
                response['status'] = "Error: no field"
        response['status'] = "Updated"
    else:
        response['status'] = "ERROR: Empty fields"
    return response


def get_field(request):
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
                "id": e.id,
                "name": e.name,
                "create_dt": e.create_dt,
                "author": e.author
            }
        )
    response['status'] = "ok"
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


def patch_agent(request):
    """
    :param request:
        {
            "agents":
            [
                {
                    "id": 1,
                    "name": "test2"
                },
                {
                    "id": 2,
                    "name": "test2"
                }
            ]
        }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    data = request.data
    if data['agents']:
        for e in data['agents']:
            agent = Agent.objects.filter(id=e["id"]).first()
            if agent:
                agent.name = e["name"]
                agent.save()
                response['status'] = "Updated"
            else:
                response['status'] = "ERROR: No agents"
                break
    else:
        response['status'] = "ERROR: Empty agents"
    return response


def get_agent(request):
    """
    :param request: { field: <id> }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    id = request.GET["id"][0]
    agents = Agent.objects.filter(field=id)
    response["agents"] = []
    for e in agents:
        response["agents"].append(
            {
                "id": e.id,
                "name": e.name,
                "create_dt": e.create_dt,
                "author": e.author
            }
        )
    response['status'] = "ok"
    return response


def create_field_rules(request):
    """
    :param request:
        {
            "field": <field_id>,
            "rules":
            [
                {
                    "condition": "if",
                    "action": "else",
                    "author": <author>
                },
                {
                    "condition": "if",
                    "action": "else",
                    "author": <author>
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
    field = Field.objects.filter(id=data['field']).first()
    if field:
        if data['rules']:
            for e in data['rules']:
                FieldRules(
                    field=field,
                    condition=e['condition'],
                    action=e['action'],
                    create_dt=request_time,
                    author=e['author']
                    ).save()
            response['status'] = "ok"
            return response
        else:
            response['status'] = "ERROR: Empty rules"
    else:
        response['status'] = "ERROR: no field"


def patch_field_rules(request):
    """
    :param request:
        {
            "rules":
            [
                {
                    "id": 1,
                    "condition": "if",
                    "action": "else"
                },
                {
                    "id": 2,
                    "condition": "if",
                    "action": "else"
                }
            ]
        }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    data = request.data
    if data['rules']:
        for e in data['rules']:
            field_rule = FieldRules.objects.filter(id=e['id']).first()
            if field_rule:
                field_rule.condition = e["condition"]
                field_rule.action = e["action"]
                field_rule.save()
                response['status'] = "Updated"
            else:
                response['status'] = f"Error: no field rule id={e['id']}"
        return response
    else:
        response['status'] = "ERROR: Empty rules"


def get_field_rules(request):
    """
    :param request: { field: <id> }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    id = request.GET["id"][0]
    field_rules = FieldRules.objects.filter(field=id)
    response["field_rules"] = []
    for e in field_rules:
        response["field_rules"].append(
            {
                "id": e.id,
                "condition": e.condition,
                "action": e.action,
                "create_dt": e.create_dt,
                "author": e.author
            }
        )
    response['status'] = "ok"
    return response


def create_agent_rules(request):
    """
    :param request:
        {
            "agent": <agent_id>,
            "rules":
            [
                {
                    "condition": "if",
                    "action": "else",
                    "author": <author>
                },
                {
                    "condition": "if",
                    "action": "else",
                    "author": <author>
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
    agent = Agent.objects.filter(id=data['agent']).first()
    if agent:
        if data['rules']:
            for e in data['rules']:
                AgentRules(
                    agent=agent,
                    condition=e['condition'],
                    action=e['action'],
                    create_dt=request_time,
                    author=e['author']
                    ).save()
            response['status'] = "ok"
            return response
        else:
            response['status'] = "ERROR: Empty rules"
    else:
        response['status'] = "ERROR: no agent"


def get_agent_rules(request):
    """
    :param request: { agent: <id> }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    id = request.GET["id"][0]
    agent_rules = AgentRules.objects.filter(agent=id)
    response["agent_rules"] = []
    for e in agent_rules:
        response["agent_rules"].append(
            {
                "id": e.id,
                "condition": e.condition,
                "action": e.action,
                "create_dt": e.create_dt,
                "author": e.author
            }
        )
    response['status'] = "ok"
    return response


def patch_agent_rules(request):
    """
    :param request:
        {
            "rules":
            [
                {
                    "id": 1,
                    "condition": "if",
                    "action": "else"
                },
                {
                    "id": 2,
                    "condition": "if",
                    "action": "else"
                }
            ]
        }
    :return:
        {
            "status": <status>
        }
    """
    response = {"status": "not ok"}
    data = request.data
    if data['rules']:
        for e in data['rules']:
            agent_rule = AgentRules.objects.filter(id=e['id']).first()
            if agent_rule:
                agent_rule.condition = e["condition"]
                agent_rule.action = e["action"]
                agent_rule.save()
                response['status'] = "Updated"
            else:
                response['status'] = f"Error: no field rule id={e['id']}"
        return response
    else:
        response['status'] = "ERROR: Empty rules"
