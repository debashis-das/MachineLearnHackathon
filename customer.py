
# 3rd party modules
from flask import make_response, abort

from customerdata import CUSTOMER



import allocateslot

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    return [CUSTOMER[key] for key in sorted(CUSTOMER.keys())]

def checkin(customerid,customer):
    checkin = customer.get("checkin", None)
    if customerid in CUSTOMER and customerid is not None:
        CUSTOMER[customerid] = {
            "customerid": customerid,
            "checkin": checkin,
            "checkintime": get_timestamp()
        }
        predictedval = allocateslot.predictslot(customerid,"2019-04-05 21:00:00")
        return make_response("slot={slot}".
                             format(slot=predictedval), 201)

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Customer with {customerid} do not exist".format(customerid=customerid),
        )