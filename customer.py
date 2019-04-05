
# 3rd party modules
from flask import make_response, abort
import json
from customerdata import CUSTOMER



import allocateslot

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    return [CUSTOMER[key] for key in sorted(CUSTOMER.keys())]

def checkin(customerid,customer):
    checkin = customer.get("checkin", None)
    if customerid in CUSTOMER and customerid is not None and checkin not in ['true','True','TRUE']:
        CUSTOMER[customerid] = {
            "customerid": customerid,
            "checkin": checkin,
            "checkintime": get_timestamp()
        }
        predictedval = allocateslot.predictslot(customerid,"2019-04-05 21:00:00")
        data = {}
        data['slot'] = predictedval
        return make_response(json.dumps(data), 200)

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Customer with {customerid} do not exist or already checked in".format(customerid=customerid),
        )