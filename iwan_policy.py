import requests
import json
requests.packages.urllib3.disable_warnings()

url = "https://192.168.1.13:443/api/v1/policy"

headers = {
    'x-auth-token': "ST-4-Bexfk7PeKKW0cbIeCrbI-cas",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "666e8991-01e5-95b9-c4b4-550ff0d91260"
    }

response = requests.request("GET", url, headers=headers, verify=False)

#print(response.text)
output = json.loads(response.text)
print json.dumps(output, indent=4)
