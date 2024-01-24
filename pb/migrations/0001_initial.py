# Generated by Django 5.0.1 on 2024-01-24 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('create_dt', models.DateTimeField(default=None, null=True)),
                ('author', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('create_dt', models.DateTimeField(default=None, null=True)),
                ('author', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='AgentRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=512)),
                ('action', models.CharField(max_length=512)),
                ('create_dt', models.DateTimeField(default=None, null=True)),
                ('author', models.CharField(max_length=512, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pb.agent')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pb.field'),
        ),
        migrations.CreateModel(
            name='FieldRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=512)),
                ('action', models.CharField(max_length=512)),
                ('create_dt', models.DateTimeField(default=None, null=True)),
                ('author', models.CharField(max_length=512, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pb.field')),
            ],
        ),
    ]