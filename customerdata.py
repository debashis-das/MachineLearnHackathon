# Data to serve with our API
# System modules
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

CUSTOMER = {
    "123453": {
        "customerid" : "123453",
        "checkin": "true",
        "checkintime": "2019-04-05 11:25:05",
    },
    "123456": {
        "customerid" : "123456",
        "checkin": "true",
        "checkintime": "2019-04-05 11:25:05",
    },
    "213456": {
        "customerid" : "213456",
        "checkin": "true",
        "checkintime": "2019-04-05 11:25:05",
    },
    "213459": {
        "customerid" : "213459",
        "checkin": "true",
        "checkintime": "2019-04-05 11:25:05",
    },
    "213458": {
        "customerid" : "213458",
        "checkin": "false",
        "checkintime": get_timestamp(),
    },
    "213457": {
        "customerid" : "213457",
        "checkin": "true",
        "checkintime": "2019-04-05 11:25:05",
    },
    "213453": {
        "customerid" : "213453",
        "checkin": "true",
        "checkintime": "2019-04-05 11:25:05",
    },
    "122457": {
        "customerid" : "122457",
        "checkin": "true",
        "checkintime": "2019-04-05 11:25:05",
    },
}

