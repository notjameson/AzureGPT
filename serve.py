import json
import requests
import urllib.parse

import quart
import quart_cors
from quart import request

# Note: Setting CORS to allow chat.openapi.com is only required when running a localhost plugin
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")
HOST_URL = "https://prices.azure.com/api/retail/prices"

def buildQueryString(regionName, serviceFamily, productName):
  base_string = '?$filter=armRegionName eq \'' + regionName + '\' and serviceFamily eq \'' + serviceFamily + '\' and productName eq \'' + productName + '\''
  return base_string
    

@app.get("/pricing")
async def get_pricing():
    regionName = request.args.get("armRegionName")
    serviceFamily = request.args.get("serviceFamily")
    serviceName = request.args.get("productName")
    url = HOST_URL + buildQueryString(regionName, serviceFamily, serviceName)
    print(url)
    res = requests.get(url)
    body = res.json()
    # concatenating for response length limitation
    body['Items'] = body['Items'][:5]
    print(body)
    return quart.Response(response=json.dumps(body), status=200)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    print("well")
    host = request.headers['Host']
    with open(".well-known/ai-plugin.json") as f:
        text = f.read()
        # This is a trick we do to populate the PLUGIN_HOSTNAME constant in the manifest
        text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
        return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    print("here")
    with open("openapi.yaml") as f:
        text = f.read()
        text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
        return quart.Response(text, mimetype="text/yaml")


def main():
    app.run(debug=True, host="0.0.0.0", port=5001)


if __name__ == "__main__":
    main()