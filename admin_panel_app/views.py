from django.shortcuts import render
from django.http import JsonResponse
from .models import MongoDBInstance, Database, User

def list_instances(request):
    instances = MongoDBInstance.objects.all()
    data = [{'name': instance.name, 'databases': instance.database_set.count(), 'users': instance.user_set.count()} for instance in instances]
    return JsonResponse({'instances': data})

# Add views for database management, user management, and authentication restrictions
