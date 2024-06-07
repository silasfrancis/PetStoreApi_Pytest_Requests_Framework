from endpoints import UserRoutes
import json
from utilities.customLogger import LogGen
from utilities import utilities


logger = LogGen.loggen()


logger.info("**************** Starting User Module Test *****************")
def test_CreateUser():
    logger.info("**************** Creating User *****************")
    response = UserRoutes.createUser()
    if response.status_code==200:
        assert True
        logger.info("**************** User Created *****************")
    else:
        logger.info("**************** Failed to Create User *****************")
        assert False


def test_GetUserData():
    logger.info("**************** Getting User Info *****************")
    response = UserRoutes.getUser()
    if response.status_code==200:
        assert True
        logger.info("**************** User Info Displayed *****************")
    else:
        logger.info("**************** Getting User Info Failed *****************")
        assert False

    data_res= response.json()
    data_str = json.dumps(data_res, indent=4)
    print(data_str)

    logger.info("**************** Validating User Data *****************")
    data = utilities.readingJsonResponseFile("UserResponse.json")
    user_id = data["id"]
    firstname = data["firstName"]

    assert data_res["id"]== user_id
    assert data_res["firstName"]== firstname
    logger.info("**************** User Data Validated *****************")

def test_UpdateUserData():
    logger.info("**************** Updating User Info *****************")
    response = UserRoutes.updateUser()
    if response.status_code==200:
        assert True
        logger.info("**************** User Data Updated *****************")
    else:
        logger.info("**************** Update not Successful *****************")
        assert False

    data_res = response.json()
    data_str = json.dumps(data_res, indent=4)
    print(data_str)

    logger.info("**************** Validating Updated Data *****************")
    data = utilities.readingJsonResponseFile("UserResponse.json")
    user_id = data["id"]

    if data_res["code"]== 200 and data_res["message"] == user_id:
        assert True
        logger.info("**************** Updated Data Validated *****************")
    else:
        logger.info("**************** Updated Data Validation Failed*****************")

def test_deleteUser():
    logger.info("**************** Deleting User *****************")
    response = UserRoutes.deleteUser()
    if response.status_code==200:
        assert True
        logger.info("**************** User Deleted*****************")
        logger.info("**************** User Module Test Passed *****************")
    else:
        logger.info("**************** Deleting User Failed *****************")
        assert False





