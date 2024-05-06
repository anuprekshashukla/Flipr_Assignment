from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MongoDBInstance, Database, User

@admin.register(MongoDBInstance)
class MongoDBInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'port')

@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instance')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
