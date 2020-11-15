from typing import Optional
from fastapi import FastAPI
import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from pydantic import BaseModel
import socket
import os

app = FastAPI()

#k8s_getter_service = "http://127.0.0.1:8081"
#k8s_putter_service = "http://127.0.0.1:8082"

#os.environ['no_proxy'] = '127.0.0.1,localhost'
k8s_getter_service = "http://getter_container:8081"
k8s_putter_service = "http://putter_container:8082"


def pod_name():
    return {"hostname": socket.gethostname(), "imz_fqdn": socket.getfqdn()}


@app.get("/")
def read_root():
    return {"Hello": "World"}


class PutterItem(BaseModel):
    item_id: int
    item_name: str


@app.get("/myapp")
def frontend_get():

    getter_service = k8s_getter_service + "/getter"
    #session = requests.Session()
    #session.trust_env = False
    response = requests.get(getter_service, verify=False)
    #response = session.get(getter_service, verify=False)
    print("frontend reponse: {}".format(response.text))
    return response.json()


@app.post("/myapp/")
def frontend_post(item: PutterItem):

    putter_service = k8s_putter_service + "/putter/"
    params = {'item_id': item.item_id, 'item_name': item.item_name}
    print("params: {}".format(params))
    session = requests.Session()
    session.trust_env = False
    response = session.post(putter_service, json=params, verify=False)
    print("Frontend Post to putter response: {}".format(response))
    return {"fronend_pod": pod_name(), "response":response.json()}
