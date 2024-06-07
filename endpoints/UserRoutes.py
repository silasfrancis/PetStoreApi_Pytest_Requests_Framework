import requests
from endpoints import Endpoints
from payload import UserPayload
from utilities import utilities
import random
import string


payload = UserPayload.payload()

def createUser():
    url = Endpoints.postUrl()
    response = requests.post(url, json=payload)

    feedback = {
        "id": payload["id"],
        "username" : payload["username"],
        "firstName" : payload["firstName"],
        "lastName": payload["lastName"],
        "email": payload["email"],
        "password": payload["password"],
        "phone": payload["phone"],
        "userStatus": payload["userStatus"]
        }
    utilities.savingJsonResponseFile("UserResponse.json", feedback)
    return response

def getUser():
    data = utilities.readingJsonResponseFile("UserResponse.json")
    username = data["username"]
    get_url = Endpoints.getUrl(username)
    get_response = requests.get(get_url)
    return get_response


def updateUser():
    data = utilities.readingJsonResponseFile("UserResponse.json")
    username = data["username"]

    updated_data = {
        "id": data["id"],
        "username": data["username"],
        "firstName": ran,
        "lastName": ran,
        "email": ran_email,
        "password": data["password"],
        "phone": data["phone"],
        "userStatus": data["userStatus"]
    }
    utilities.savingJsonResponseFile("UserResponse.json", updated_data)

    update_url = Endpoints.updateUrl(username)
    update_response = requests.put(update_url, json=updated_data)
    return update_response


def deleteUser():
    data = utilities.readingJsonResponseFile("UserResponse.json")
    username = data["username"]
    delete_url = Endpoints.deleteUrl(username)
    delete_response = requests.delete(delete_url)
    feedback = {

    }
    utilities.savingJsonResponseFile("UserResponse.json", feedback)
    return delete_response

n = 7
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
ran_email = ran + "@gmail.com"

