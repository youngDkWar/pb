from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=512)
    create_dt = models.DateTimeField(null=True, default=None)
    author = models.CharField(max_length=512)


class FieldRules(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    condition = models.CharField(max_length=512)
    action = models.CharField(max_length=512)
    create_dt = models.DateTimeField(null=True, default=None)
    author = models.CharField(null=True, max_length=512)


class Agent(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    create_dt = models.DateTimeField(null=True, default=None)
    author = models.CharField(null=True, max_length=512)


class AgentRules(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    condition = models.CharField(max_length=512)
    action = models.CharField(max_length=512)
    create_dt = models.DateTimeField(null=True, default=None)
    author = models.CharField(null=True, max_length=512)

