from pydoc import describe
from tkinter import CASCADE
from tkinter.tix import Tree
from turtle import Turtle
from django.db import models
from sqlalchemy import true
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host =  models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)

    
    name = models.CharField(max_length=200)
    # can't not be null
    description = models.TextField(null=True,blank=True)
    # user in room
    
    # 多对多
    participants = models.ManyToManyField(User,related_name='participants',blank=True)


    updated = models.DateTimeField(auto_now=True)
    # never changed
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)

    # 一对多
    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    body = models.TextField()
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[0:50]


