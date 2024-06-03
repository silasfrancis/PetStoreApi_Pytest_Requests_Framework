base_url= "https://petstore.swagger.io/v2"

#[User module]
def postUrl():
    post_url = base_url + "/user"
    return post_url

def getUrl(username):
    get_url= base_url + f"/user/{username}"
    return get_url

def updateUrl(username):
    update_url= base_url + f"/user/{username}"
    return update_url

def deleteUrl(username):
    delete_url= base_url + f"/user/{username}"
    return delete_url

#[Store module]
def postOrderUrl():
    post_order_url= base_url + "/store/order"
    return post_order_url

def getorderUrl(orderId):
    get_order_url= base_url + f"/store/order/{orderId}"
    return get_order_url

def deleteOrderUrl(orderId):
    delete_order_url= base_url + f"/store/order/{orderId}"
    return delete_order_url

#[Pet module]
def postPetUrl():
    post_pet_url= base_url +"/pet"
    return post_pet_url

def getPetUrl(petid):
    get_pet_url = base_url+ f"/pet/{petid}"
    return get_pet_url

def updatePetUrl():
    update_pet_url= base_url+"/pet"
    return update_pet_url

def deletePetUrl(petid):
    delete_pet_url = base_url+ f"/pet/{petid}"
    return delete_pet_url
