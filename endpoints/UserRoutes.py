import requests
from endpoints import Endpoints
from payload import UserPayload
import json
import random
import string


payload = UserPayload.payload()

n = 7
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
ran_email = ran + "@gmail.com"

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
    save_file = open("UserResponse.json", "w")
    json.dump(feedback, save_file, indent = 4)
    save_file.close()

    return response

def getUser():
    with open ('UserResponse.json', 'r') as file:
        data = json.load(file)
    username = data["username"]

    get_url = Endpoints.getUrl(username)
    get_response = requests.get(get_url)
    return get_response


def updateUser():
    with open ('UserResponse.json', 'r') as file:
        data = json.load(file)
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
    save_file = open("UserResponse.json", "w")
    json.dump(updated_data, save_file, indent = 4)
    save_file.close()

    update_url = Endpoints.updateUrl(username)
    update_response = requests.put(update_url, json=updated_data)
    return update_response


def deleteUser():
    with open ('UserResponse.json', 'r') as file:
        data = json.load(file)
    username = data["username"]

    delete_url = Endpoints.deleteUrl(username)
    delete_response = requests.delete(delete_url)

    # feedback = {
    #
    # }
    # save_file = open("UserResponse.json", "w")
    # json.dump(feedback, save_file, indent = 4)
    # save_file.close()

    return delete_response



