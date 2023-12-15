from django.shortcuts import render
import numpy as np
from celery import Celery
from celery import shared_task
from celery.schedules import crontab


app = Celery()

from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import os
from .models import canal1, canal2, canal3, canal4,canal5,canal6,canal7,canal8,canal9,canal10,canal11,canal12

ipsensor ='192.168.1.101'

@app.task
def modbustcp(x,y):
        try:
            datos = [canal1, canal2, canal3, canal4,canal5,canal6,canal7,canal8,canal9,canal10,canal11,canal12]
            for i in range(12):
                client = ModbusClient(host=ipsensor,unit_id=i+x,port=y,auto_open=True,timeout=10.5)
                result = client.read_input_registers(1,70)
                container=[utils.decode_ieee(tl) for tl in utils.word_list_to_long(result)]
                
                datos[i].objects.create(V1 = container[0], V2 = container[1], V3 = container[2], VB12 = container[3], VB23 = container[4], VB31 = container[5], C1 = container[6], C2 = container[7], C3 = container[8], AP1 = container[9], AP2 = container[10], AP3 = container[11], TAP = container[12], ApP1 = container[13], ApP2 = container[14], ApP3 = container[15], TApP = container[16], R1 = container[17], R2 = container[18], R3 = container[19], TRP = container[20], PF1 = container[21], PF2 = container[22], PF3 = container[23], TPF = container[24], F1 = container[25], F2 = container[26], F3 = container[27], CN = container[28], PF1C = container[29], PF2C = container[30], PF3C = container[31], TPFS = container[32], TC = container[33], LC = container[34])
                client.close()
        except:
            print('No se guardaron los datos')