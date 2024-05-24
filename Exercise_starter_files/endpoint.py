import requests
import json

# # URL for the web service, should be similar to:
# # 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
# scoring_uri = "http://a471b2aa-2452-436a-8dc0-57148f358828.southcentralus.azurecontainer.io/score"

# # If the service is authenticated, set the key or token
# key = ""

# # Two sets of data to score, so we get two results back
# data = {
#     "data": [
#         {
#             "instant": 1,
#             "date": "2013-01-01 00:00:00,000000",
#             "season": 1,
#             "yr": 0,
#             "mnth": 1,
#             "weekday": 6,
#             "weathersit": 2,
#             "temp": 0.344167,
#             "atemp": 0.363625,
#             "hum": 0.805833,
#             "windspeed": 0.160446,
#             "casual": 331,
#             "registered": 654,
#         },
#     ]
# }

# data={
# "data":[
#     {"age":57,"job":"technician","marital":"married","education":"high.school","default":"no","housing":"no","loan":"yes","contact":"cellular","month":"may","day_of_week":"mon","duration":371,"campaign":1,"pdays":999,"previous":1,"poutcome":"failure","emp.var.rate":-1.8,"cons.price.idx":92.893,"cons.conf.idx":-46.2,"euribor3m":1.299,"nr.employed":5099.1}
# ]





import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
      "data":[
    {"age":57,"job":"technician","marital":"married","education":"high.school","default":"no","housing":"no","loan":"yes","contact":"cellular","month":"may","day_of_week":"mon","duration":371,"campaign":1,"pdays":999,"previous":1,"poutcome":"failure","emp.var.rate":-1.8,"cons.price.idx":92.893,"cons.conf.idx":-46.2,"euribor3m":1.299,"nr.employed":5099.1}
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

url = 'http://a471b2aa-2452-436a-8dc0-57148f358828.southcentralus.azurecontainer.io/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = ''
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



# # Convert to JSON string
# input_data = json.dumps(data)
# with open("data.json", "w") as _f:
#     _f.write(input_data)

# # Set the content type
# headers = {"Content-Type": "application/json"}
# # If authentication is enabled, set the authorization header
# headers["Authorization"] = f"Bearer {key}"

# # Make the request and display the response
# resp = requests.post(scoring_uri, input_data, headers=headers)
# print(resp.json())
