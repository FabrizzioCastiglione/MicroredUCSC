from django.urls import re_path
from .consumers import GraphConsumer, Potencia_Activa, FactorPotencia


ws_urlpatterns= [
    re_path(r"^ws/graph/$", GraphConsumer.as_asgi()),
    re_path(r"^ws/Potencia_Activa/$", Potencia_Activa.as_asgi()),
    re_path(r"^ws/FactorPotencia/$", FactorPotencia.as_asgi()),
]
