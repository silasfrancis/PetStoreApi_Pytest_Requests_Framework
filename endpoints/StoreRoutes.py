import requests
from endpoints import Endpoints
from payload import StorePayload
import json


payload = StorePayload.payload()

def placeOrder():
    url = Endpoints.postOrderUrl()
    response = requests.post(url, json=payload)

    feedback = {
        "id": payload["id"],
        "petId": payload["petId"],
        "quantity": payload["quantity"],
        "shipDate": payload["shipDate"],
        "status": payload["status"],
        "complete": payload["complete"]
    }
    save_file = open("StoreResponse.json", "w")
    json.dump(feedback, save_file, indent = 6)
    save_file.close()

    return response


def getOrder():
    with open('StoreResponse.json', 'r') as file:
        data = json.load(file)
    id = data["id"]

    url = Endpoints.getorderUrl(id)
    response = requests.get(url)
    return response

def deleteOrder():
    with open ('StoreResponse.json', 'r') as file:
        data = json.load(file)
    id = data["id"]

    url = Endpoints.deleteOrderUrl(id)
    response = requests.delete(url)
    feedback = {

    }
    save_file = open("StoreResponse.json", "w")
    json.dump(feedback, save_file, indent = 6)
    save_file.close()
    return response

