from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

CUSTOMERSLOT = {
    "123453": {
        "customerid" : "123453",
        "orderId": "7365190717340",
        "total" : "300",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
    "123456": {
        "customerid" : "123456",
        "orderId": "7365190717340",
        "total" : "320",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
    "213456": {
        "customerid" : "213456",
        "orderId": "7365190717340",
        "total" : "325",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
    "213459": {
        "customerid" : "213459",
        "orderId": "7365190717340",
        "total" : "400",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
    "213458": {
        "customerid" : "213458",
        "orderId": "7365190717340",
        "total" : "420",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
    "213457": {
        "customerid" : "213457",
        "orderId": "7365190717340",
        "total" : "450",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
    "213453": {
        "customerid" : "213453",
        "orderId": "7365190717340",
        "total" : "540",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
    "122457": {
        "customerid" : "122457",
        "orderId": "7365190717340",
        "total" : "430",
        "allocatedslot":"11.00AM-12.00PM",
        "checkintime": get_timestamp(),
    },
}