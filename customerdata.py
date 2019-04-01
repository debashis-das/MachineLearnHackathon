# Data to serve with our API
# System modules
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

CUSTOMER = {
    "123453": {
        "customerid" : "123453",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "123456": {
        "customerid" : "123456",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "213456": {
        "customerid" : "213456",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "123459": {
        "customerid" : "213459",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "213458": {
        "customerid" : "213458",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "213457": {
        "customerid" : "213457",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "213453": {
        "customerid" : "213453",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "122457": {
        "customerid" : "122457",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
}

