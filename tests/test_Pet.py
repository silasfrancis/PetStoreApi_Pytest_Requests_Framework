from endpoints import PetRoutes
import json
from utilities.customLogger import LogGen
from utilities import utilities

logger = LogGen.loggen()


logger.info("**************** Starting Store Module Test *****************")
def test_addPet():
    logger.info("**************** Adding Pet *****************")
    response = PetRoutes.addPet()
    if response.status_code==200:
        assert True
        logger.info("**************** Pet Added Successfully *****************")
    else:
        logger.info("**************** Failed to Add Pet *****************")

def test_getPet():
    logger.info("**************** Getting Pet Info *****************")
    response = PetRoutes.getPet()
    if response.status_code==200:
        assert True
        logger.info("**************** Pet Info Fetched *****************")
    else:
        logger.info("**************** Failed to Fetch Pet Info *****************")
        assert False

    data_res= response.json()
    data_str = json.dumps(data_res, indent=4)
    print(data_str)

    logger.info("**************** Validating Pet Data *****************")
    data = utilities.readingJsonResponseFile("PetResponse.json")
    pet_name = data["name"]
    tag_id = data["tags"][0]["id"]
    tag_name = data["tags"][0]["name"]
    status = data["status"]

    if data_res["name"] == pet_name:
        assert True
    elif data_res["tags"][0]["id"] == tag_id:
        assert True
    elif data_res["tags"][0]["name"] == tag_name:
        assert True
    elif data_res["status"] == status:
        assert True
        logger.info("**************** Pet Data Validation Successful *****************")
    else:
        logger.info("**************** Pet Data Validation Failed *****************")
        assert False

def test_updatePet():
    logger.info("**************** Updating Pet Data *****************")
    response = PetRoutes.updatePet()
    if response.status_code==200:
        assert True
        logger.info("**************** Pet Data Updated*****************")
    else:
        logger.info("**************** Updating Pet Data Failed*****************")
        assert False
    data_res= response.json()
    data_str = json.dumps(data_res, indent=4)
    print(data_str)

    logger.info("**************** Validating Updated Pet Data *****************")
    data = utilities.readingJsonResponseFile("PetResponse.json")
    pet_name = data["name"]
    tag_name = data["tags"][0]["name"]
    status = data["status"]

    if data_res["name"] == pet_name:
        assert True
    elif data_res["tags"][0]["name"] == tag_name:
        assert True
    elif data_res["status"] == status:
        assert True
        logger.info("**************** Pet Data Validation Successful *****************")
    else:
        logger.info("**************** Pet Data Validation Failed *****************")
        assert False

def test_deletePet():
    logger.info("**************** Deleting Pet *****************")
    response = PetRoutes.deletePet()
    if response.status_code==200:
        assert True
        logger.info("**************** Pet Deleted *****************")
        logger.info("**************** Pet Module Test Passed *****************")
    else:
        logger.info("**************** Failed to Delete Pet *****************")


