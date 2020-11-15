from typing import Optional
from fastapi import FastAPI
import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import socket
import os

app = FastAPI()


#k8s_putter_service = "http://127.0.0.1:8082/" + "putter"
k8s_putter_service = "http://putter_container:8082/" + "putter"


def pod_name():
    return {"hostname": socket.gethostname(), "imz_fqdn": socket.getfqdn()}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/getter/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/getter")
def getter():
    #session = requests.session()
    #session.trust_env = False

    response = requests.get(k8s_putter_service, verify=False)
    return {"getter_pod": pod_name(), "response": response.json()}



