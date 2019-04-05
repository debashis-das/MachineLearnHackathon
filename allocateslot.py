
import pandas as pd
from fbprophet import Prophet
import json
from customersslot import CUSTOMERSLOT
from slot import SLOT

def predict(csvname,predictdate):
    # Importing the dataset
    dataset = pd.read_csv("customers/"+csvname+".csv")
    dataset.head()
    m = Prophet(changepoint_prior_scale=0.1)
    m.fit(dataset)
    data = [predictdate]
    future = pd.DataFrame(data,columns=['ds'])
    #future.head()
    forecast = m.predict(future)
    return forecast.to_json(orient='records')[1:-1].replace('},{', '} {')

def predictslot(customerid,predictdate):
    predictedval = predict(customerid,predictdate)
    jsondata = json.loads(predictedval)
    
    if jsondata['yhat'] < 15 and len(SLOT["1"]) != 2 :
        SLOT["1"].append(CUSTOMERSLOT[customerid])
        return 1
    elif jsondata['yhat'] < 30 and len(SLOT["2"]) != 2 :
        SLOT["2"].append(CUSTOMERSLOT[customerid])
        return 2
    elif jsondata['yhat'] < 45 and len(SLOT["3"]) != 2 :
        SLOT["3"].append(CUSTOMERSLOT[customerid])
        return 3
    elif jsondata['yhat'] > 45 and len(SLOT["4"]) != 2 :
        SLOT["4"].append(CUSTOMERSLOT[customerid])
        return 4
    else :
        SLOT["generic"].append(CUSTOMERSLOT[customerid])
        return -1
        
        