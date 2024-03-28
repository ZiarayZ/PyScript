from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=255, unique=True, primary_key=True)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    permissions = models.IntegerField(default=1)


class Messages(models.Model):
    messageid = models.AutoField(unique=True, primary_key=True)
    content = models.CharField(max_length=255)
    createdon = models.DateTimeField()
    spoiler = models.BooleanField(default=False)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
