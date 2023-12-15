from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep


import numpy as np
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import canal1, canal2, canal3, canal4,canal5,canal6,canal7,canal8,canal9,canal10,canal11,canal12



class GraphConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()

    for i in range(1000):
      await self.send(json.dumps({'value':randint(1,100)}))
      await sleep(1)
      
      
      
      
class Potencia_Activa(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()
    idmax = canal12.objects.latest('id').id
    objs1 = canal1.objects.all()[canal1.objects.latest('id').id-1:]
    objs2 = canal2.objects.all()[canal2.objects.latest('id').id-1:]
    objs3 = canal3.objects.all()[canal3.objects.latest('id').id-1:]
    objs4 = canal4.objects.all()[canal4.objects.latest('id').id-1:]
    objs5 = canal5.objects.all()[canal5.objects.latest('id').id-1:]
    objs6 = canal6.objects.all()[canal6.objects.latest('id').id-1:]
    objs7 = canal7.objects.all()[canal7.objects.latest('id').id-1:]
    objs8 = canal8.objects.all()[canal8.objects.latest('id').id-1:]
    objs9 = canal9.objects.all()[canal9.objects.latest('id').id-1:]
    objs10 = canal10.objects.all()[canal10.objects.latest('id').id-1:]
    objs11 = canal11.objects.all()[canal11.objects.latest('id').id-1:]
    objs12 = canal12.objects.all()[canal12.objects.latest('id').id-1:]
    P1 =[]
    P2 =[]
    P3 =[]
    P4 =[]
    P5 =[]
    P6 =[]
    P7 =[]
    P8 =[]
    P9 =[]
    P10 =[]
    P11 =[]
    P12 =[]
    PotenciaTotal =[]
    for i in range(len(objs1)):
        P1.append(objs1[i].TAP)
        P2.append(objs2[i].TAP)
        P3.append(objs3[i].TAP)
        P4.append(objs4[i].TAP)
        P5.append(objs5[i].TAP)
        P6.append(objs6[i].TAP)
        P7.append(objs7[i].TAP)
        P8.append(objs8[i].TAP)
        P9.append(objs9[i].TAP)
        P10.append(objs10[i].TAP)
        P11.append(objs11[i].TAP)
        P12.append(objs12[i].TAP)
        PotenciaTotal = ((P1[i]+P2[i]+P3[i]+P4[i]+P5[i]+P6[i]+P7[i]+P8[i]+P9[i]+P10[i]+P11[i]+P12[i]))
    data = {
      'Potencia_Activa': PotenciaTotal,
    }
    await self.send(json.dumps(data))     
      
      

class PotenciaReactiva(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()
    idmax = canal12.objects.latest('id').id
    objs1 = canal1.objects.all()[canal1.objects.latest('id').id-1:]
    objs2 = canal2.objects.all()[canal2.objects.latest('id').id-1:]
    objs3 = canal3.objects.all()[canal3.objects.latest('id').id-1:]
    objs4 = canal4.objects.all()[canal4.objects.latest('id').id-1:]
    objs5 = canal5.objects.all()[canal5.objects.latest('id').id-1:]
    objs6 = canal6.objects.all()[canal6.objects.latest('id').id-1:]
    objs7 = canal7.objects.all()[canal7.objects.latest('id').id-1:]
    objs8 = canal8.objects.all()[canal8.objects.latest('id').id-1:]
    objs9 = canal9.objects.all()[canal9.objects.latest('id').id-1:]
    objs10 = canal10.objects.all()[canal10.objects.latest('id').id-1:]
    objs11 = canal11.objects.all()[canal11.objects.latest('id').id-1:]
    objs12 = canal12.objects.all()[canal12.objects.latest('id').id-1:]
    TRP1 =[]
    TRP2 =[]
    TRP3 =[]
    TRP4 =[]
    TRP5 =[]
    TRP6 =[]
    TRP7 =[]
    TRP8 =[]
    TRP9 =[]
    TRP10 =[]
    TRP11 =[]
    TRP12 =[]
    PotenciaReactiva =[]
    for i in range(len(objs1)):
      TRP1.append(objs1[i].TRP)
      TRP2.append(objs2[i].TRP)
      TRP3.append(objs3[i].TRP)
      TRP4.append(objs4[i].TRP)
      TRP5.append(objs5[i].TRP)
      TRP6.append(objs6[i].TRP)
      TRP7.append(objs7[i].TRP)
      TRP8.append(objs8[i].TRP)
      TRP9.append(objs9[i].TRP)
      TRP10.append(objs10[i].TRP)
      TRP11.append(objs11[i].TRP)
      TRP12.append(objs12[i].TRP)
      PotenciaReactiva.append((TRP1[i]+TRP2[i]+TRP3[i]+TRP4[i]+TRP5[i]+TRP6[i]+TRP7[i]+TRP8[i]+TRP9[i]+TRP10[i]+TRP11[i]+TRP12[i])/12)
    data = {
      'PotenciaReactiva': PotenciaReactiva,
    }
    await self.send(json.dumps(data))
  
  
class FactorPotencia(AsyncWebsocketConsumer):
   async def connect(self):
    await self.accept()
    idmax = canal12.objects.latest('id').id
    objs1 = canal1.objects.all()[canal1.objects.latest('id').id-1:]
    objs2 = canal2.objects.all()[canal2.objects.latest('id').id-1:]
    objs3 = canal3.objects.all()[canal3.objects.latest('id').id-1:]
    objs4 = canal4.objects.all()[canal4.objects.latest('id').id-1:]
    objs5 = canal5.objects.all()[canal5.objects.latest('id').id-1:]
    objs6 = canal6.objects.all()[canal6.objects.latest('id').id-1:]
    objs7 = canal7.objects.all()[canal7.objects.latest('id').id-1:]
    objs8 = canal8.objects.all()[canal8.objects.latest('id').id-1:]
    objs9 = canal9.objects.all()[canal9.objects.latest('id').id-1:]
    objs10 = canal10.objects.all()[canal10.objects.latest('id').id-1:]
    objs11 = canal11.objects.all()[canal11.objects.latest('id').id-1:]
    objs12 = canal12.objects.all()[canal12.objects.latest('id').id-1:]
    TRP1 =[]
    TRP2 =[]
    TRP3 =[]
    TRP4 =[]
    TRP5 =[]
    TRP6 =[]
    TRP7 =[]
    TRP8 =[]
    TRP9 =[]
    TRP10 =[]
    TRP11 =[]
    TRP12 =[]
    FactorPotenciaTotal =[]
    for i in range(len(objs1)):
      TRP1.append(objs1[i].TRP)
      TRP2.append(objs2[i].TRP)
      TRP3.append(objs3[i].TRP)
      TRP4.append(objs4[i].TRP)
      TRP5.append(objs5[i].TRP)
      TRP6.append(objs6[i].TRP)
      TRP7.append(objs7[i].TRP)
      TRP8.append(objs8[i].TRP)
      TRP9.append(objs9[i].TRP)
      TRP10.append(objs10[i].TRP)
      TRP11.append(objs11[i].TRP)
      TRP12.append(objs12[i].TRP)
      PotenciaReactiva.append((TRP1[i]+TRP2[i]+TRP3[i]+TRP4[i]+TRP5[i]+TRP6[i]+TRP7[i]+TRP8[i]+TRP9[i]+TRP10[i]+TRP11[i]+TRP12[i]))
    data = {
      'FactorPotencia': FactorPotenciaTotal,
    }
    await self.send(json.dumps(data))