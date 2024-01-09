from channels.generic.websocket import AsyncWebsocketConsumer
import json
import os
from random import randint
from asyncio import sleep
from .models import prueba

import numpy as np
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"



class GraphConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()
    r1 = len(prueba.objects.all())
    r = prueba.objects.all()[r1-100:]
    datos = []
    tiempo = []
    for i in range(len(r)):
      datos.append(r[i].V1)
      tiempo.append(i)
      
    await self.send(json.dumps({'value':datos,'time':tiempo}))
