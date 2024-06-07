from payload import PetPayload
from endpoints import Endpoints
from utilities import utilities
import requests
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
    utilities.savingJsonResponseFile("PetResponse.json", feedback)

    return response

def getPet():
    data = utilities.readingJsonResponseFile("PetResponse.json")
    id = data["id"]
    url = Endpoints.getPetUrl(id)
    response = requests.get(url)
    return response

def updatePet():
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
    utilities.savingJsonResponseFile("PetResponse.json", updated_data)

    url = Endpoints.updatePetUrl()
    response = requests.put(url, json=updated_data)
    return response

def deletePet():
    data = utilities.readingJsonResponseFile("PetResponse.json")
    id = data["id"]
    url = Endpoints.deletePetUrl(id)
    response = requests.delete(url)
    feedback = {

    }
    utilities.savingJsonResponseFile("PetResponse.json", feedback)

    return response

n=7
ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
ran_status = random.choice(["available", "pending", "sold"])