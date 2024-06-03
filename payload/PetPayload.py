import random
import string

def payload():
    n=7
    ran_int = random.randint(999, 9999)
    ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    ran_status = random.choice(["available", "pending", "sold"])

    return{
        "id": ran_int,
        "category": {
            "id": ran_int,
            "name": ran_str
        },
        "name": ran_str,
        "photoUrls": [
            ran_str+ran_str+".com/pet/photo"
        ],
        "tags": [
            {
                "id": ran_int,
                "name": ran_str
            }
        ],
        "status": ran_status
    }