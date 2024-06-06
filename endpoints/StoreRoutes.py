import requests
from endpoints import Endpoints
from payload import StorePayload
from utilities import readingJson
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
    readingJson.savingJsonResponseFile("StoreResponse.json", feedback)
    return response


def getOrder():
    data = readingJson.readingJsonResponseFile("StoreResponse.json")
    id = data["id"]
    url = Endpoints.getorderUrl(id)
    response = requests.get(url)
    return response

def deleteOrder():
    data = readingJson.readingJsonResponseFile("StoreResponse.json")
    id = data["id"]
    url = Endpoints.deleteOrderUrl(id)
    response = requests.delete(url)
    feedback = {

    }
    readingJson.savingJsonResponseFile("StoreResponse.json", feedback)
    return response

