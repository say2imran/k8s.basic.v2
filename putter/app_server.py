from typing import Optional
from fastapi import FastAPI
import requests
import socket
from pydantic import BaseModel
import os

app = FastAPI()

#os.environ['no_proxy'] = '127.0.0.1,localhost'


def pod_name():
    return {"hostname": socket.gethostname(), "imz_fqdn": socket.getfqdn()}


putter_collection = {}


class PutterItem(BaseModel):
    item_id: int
    item_name: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/putter")
def get_item():
    return {"putter_pod": pod_name(), "putter_response": putter_collection}


@app.post("/putter/")
def put_item(item: PutterItem):
    print("Put item function: {}".format(item))
    putter_collection[item.item_id] = item.item_name
    return {"putter_pod": pod_name(), "putter_response": "Updated ITEM"}
