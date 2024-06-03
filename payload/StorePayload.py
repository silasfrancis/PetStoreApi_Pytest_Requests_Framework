import random
from datetime import timedelta, datetime


def payload():
    ran_int = random.randint(99999, 9999999)
    ran_quant = random.randint(1, 10)
    n = 7
    ran_bool = random.choice([True, False])

    d1 = datetime(2024, 6, 21, 15, 46, 13, 8010)
    d2 = datetime(2025, 6, 21, 15, 46, 13, 8010)
    ran_date = (d1 + timedelta(days= 20)).isoformat()

    return {
        "id": ran_int,
        "petId": ran_int,
        "quantity": ran_quant,
        "shipDate": ran_date,
        "status": "placed",
        "complete": ran_bool
    }