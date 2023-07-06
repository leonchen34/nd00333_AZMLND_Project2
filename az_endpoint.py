import urllib.request
import json
#import os
#import ssl

'''
def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
'''

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "data": [
      {
        "age": 0,
        "job": "example_value",
        "marital": "example_value",
        "education": "example_value",
        "default": "example_value",
        "housing": "example_value",
        "loan": "example_value",
        "contact": "example_value",
        "month": "example_value",
        "day_of_week": "example_value",
        "duration": 1000,
        "campaign": 0,
        "pdays": 0,
        "previous": 0,
        "poutcome": "example_value",
        "emp.var.rate": 0,
        "cons.price.idx": 0,
        "cons.conf.idx": 0,
        "euribor3m": 0.0,
        "nr.employed": 0
      },
          {
            "age": 87,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 471,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          }

    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

url = 'http://65598e37-767b-4966-8e42-46df2f2b50d4.eastus.azurecontainer.io/score'
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = '5JDRdlQi3BvAEkP27bH34cquWrgSo7rG'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
