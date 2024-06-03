import random
import string
def payload():
    user_id = random.randint(99999, 9999999)
    n = 7
    p= 10
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    ran_email = ran + "@gmail.com"
    ran_phone= ''.join(random.choices(string.digits, k = p))


    return {
            "id": user_id,
            "username": ran,
            "firstName": ran,
            "lastName": ran,
            "email": ran_email,
            "password": ran,
            "phone": ran_phone,
            "userStatus": 0
        }