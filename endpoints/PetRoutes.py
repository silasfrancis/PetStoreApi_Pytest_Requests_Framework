from payload import PetPayload
from endpoints import Endpoints
import requests
import json
import random
import string


payload = PetPayload.payload()

def addPet():
    url = Endpoints.postPetUrl()
    response = requests.post(url, json=payload)

    feedback = {
        "id": payload["id"],
        "category": {
            "id": payload["category"]["id"],
            "name": payload["category"]["name"]
        },
        "name": payload["name"],
        "photoUrls": [
            payload["photoUrls"]
        ],
        "tags": [
            {
                "id": payload["tags"][0]["id"],
                "name": payload["tags"][0]["name"]
            }
        ],
        "status": payload["status"]
    }
    save_file = open("PetResponse.json", "w")
    json.dump(feedback, save_file, indent = 4)
    save_file.close()

    return response

def getPet():
    with open('PetResponse.json', 'r') as file:
        data = json.load(file)
    id = data["id"]

    url = Endpoints.getPetUrl(id)
    response = requests.get(url)
    return response

def updatePet():
    n=7
    ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    ran_status = random.choice(["available", "pending", "sold"])

    updated_data = {
        "id": payload["id"],
        "category": {
            "id": payload["category"]["id"],
            "name": payload["category"]["name"]
        },
        "name": ran_str,
        "photoUrls":payload["photoUrls"],
        "tags": [
            {
                "id": payload["tags"][0]["id"],
                "name": ran_str
            }
        ],
        "status": ran_status
    }
    save_file = open("PetResponse.json", "w")
    json.dump(updated_data, save_file, indent = 4)
    save_file.close()

    url = Endpoints.updatePetUrl()
    response = requests.put(url, json=updated_data)
    return response

def deletePet():
    with open('PetResponse.json', 'r') as file:
        data = json.load(file)
    id = data["id"]

    url = Endpoints.deletePetUrl(id)
    response = requests.delete(url)
    feedback = {

    }
    save_file = open("PetResponse.json", "w")
    json.dump(feedback, save_file, indent = 4)
    save_file.close()
    return response

