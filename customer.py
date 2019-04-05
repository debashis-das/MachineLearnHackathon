
# 3rd party modules
from flask import make_response, abort
import json
from customerdata import CUSTOMER

import allocateslot
from slot import SLOT

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    return [CUSTOMER[key] for key in sorted(CUSTOMER.keys())]

def checkin(customerid,customer):
    checkin = customer.get("checkin", None)
    if customerid in CUSTOMER and customerid is not None and checkin in ['true','True','TRUE']:
        if CUSTOMER[customerid]['checkin'] not in ['true','True','TRUE']:
            CUSTOMER[customerid] = {
                "customerid": customerid,
                "checkin": checkin,
                "checkintime": get_timestamp()
            }
            predictedval = allocateslot.predictslot(customerid,"2019-04-05 21:00:00")
            data = {}
            data['slot'] = predictedval
            return make_response(json.dumps(data), 200)
        else:
            data = {}
            for customeobj in SLOT['1'] :
                if customeobj['customerid'] in [customerid]:
                    data['slot'] = 1
                    return make_response(json.dumps(data), 200)
            for customeobj in SLOT['2'] :
                if customeobj['customerid'] in [customerid]:
                    data['slot'] = 2
                    return make_response(json.dumps(data), 200)
            for customeobj in SLOT['3'] :
                if customeobj['customerid'] in [customerid]:
                    data['slot'] = 3
                    return make_response(json.dumps(data), 200)
            for customeobj in SLOT['4'] :
                if customeobj['customerid'] in [customerid]:
                    data['slot'] = 4
                    return make_response(json.dumps(data), 200)
            for customeobj in SLOT['generic'] :
                if customeobj['customerid'] in [customerid]:
                    data['slot'] = -1
                    return make_response(json.dumps(data), 200)
    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Customer with {customerid} do not exist".format(customerid=customerid),
        )