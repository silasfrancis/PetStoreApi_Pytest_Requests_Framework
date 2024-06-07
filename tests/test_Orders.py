from endpoints import StoreRoutes
import json
from payload import StorePayload
from utilities.customLogger import LogGen
from utilities import utilities


logger = LogGen.loggen()
payload = StorePayload.payload()

logger.info("**************** Starting Store Module Test *****************")
def test_placeOrder():
    logger.info("**************** Placing Order *****************")
    response = StoreRoutes.placeOrder()
    if response.status_code==200:
        assert True
        logger.info("**************** Order Placed *****************")
    else:
        logger.info("**************** Place Order Failed *****************")
        assert False

def test_getOrderInfo():
    logger.info("**************** Getting Order Info *****************")
    response = StoreRoutes.getOrder()
    if response.status_code==200:
        assert True
        logger.info("**************** Order Info Displayed *****************")
    else:
        logger.info("**************** Failed to Fetch Order Info *****************")
        assert False

    data_res= response.json()
    data_str = json.dumps(data_res, indent=4)
    print(data_str)

    logger.info("**************** Validating Order Info *****************")
    data = utilities.readingJsonResponseFile("StoreResponse.json")
    petid = data["petId"]
    quantity = data["quantity"]

    if data_res["petId"] == petid and data_res["quantity"] == quantity:
        assert True
        logger.info("**************** Order Info Validation Successful *****************")
    else:
        logger.info("**************** Order Info Validation Failed *****************")

def test_deleteOrder():
    logger.info("**************** Deleting Order *****************")
    response = StoreRoutes.deleteOrder()
    if response.status_code==200:
        assert True
        logger.info("**************** Order Deleted *****************")
        logger.info("**************** Store Module Test Passed *****************")
    else:
        logger.info("**************** Deleting Order Failed *****************")



