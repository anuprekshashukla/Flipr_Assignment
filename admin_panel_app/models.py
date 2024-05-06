from django.db import models

class MongoDBInstance(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.IntegerField()

class Database(models.Model):
    name = models.CharField(max_length=100)
    instance = models.ForeignKey(MongoDBInstance, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    databases = models.ManyToManyField(Database)
