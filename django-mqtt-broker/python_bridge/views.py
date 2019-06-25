from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import paho.mqtt.client as mqtt


greeting = """
<HTML>

<HEAD>

<TITLE>Python HTTP -> MQTT bridge</TITLE>

</HEAD>

<BODY BGCOLOR="3399ff" text="white">
<center>
    <h1>Hi :)</h1>

    <h2>The MQTT bridge is working fine :D</h2>
    <h3>by fig0!</h3>
</center>
</BODY>

</HTML>
"""


def index(request):
    # template = loader.get_template('python_bridge/index.html')
    return HttpResponse(greeting)

# Create your views here.
def pub(request, topic, payload):
    client = mqtt.Client()

    client.username_pw_set("samuel.chenatti@gmail.com", "***")
    client.connect("maqiatto.com", 1883, 60)

    status = client.publish("samuel.chenatti@gmail.com/"+topic, payload=payload)

    return HttpResponse("Publish in topic {} payload {}".format("samuel.chenatti@gmail.com/"+topic, payload))
