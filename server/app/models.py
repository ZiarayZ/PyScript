from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=255, unique=True, primary_key=True)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Channels(models.Model):
    channelid = models.AutoField(unique=True, primary_key=True)

    # message bounds and another table for messages using a foreign key...? How do?


class Messages(models.Model):
    messageid = models.AutoField(unique=True, primary_key=True)
    content = models.CharField(max_length=255)
