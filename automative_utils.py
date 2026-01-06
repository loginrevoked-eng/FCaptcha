import fastapi
import config
from records_and_metrics import recorddDelivery
import os




def raiseNotMainErrorAndExit(file,name):
    raise ImportError(
        f"the file {file} can not be imported in {name}"+
        f"ran the {file} alone using [ < python {file} > ]"
    )

def ServerStartUp(filename,name):
    if name != "__main__":return None
    print(f"StartUp func called from __file__:{filename} and __name__:{name}")
    import os
    import colorama
    colorama.init(autoreset=True)
    os.system(
        getUvicornRunCommand()
    )


def getUvicornRunCommand():
    command = (
        f"uvicorn {config.ServerFile.replace('.py','')}:app"
        f" --port {config.DeployedPort}"
        f" --host {"127.0.0.1" if config.host == "localhost" else config.host}"
        f" --no-server-header --no-date-header --no-access-log {'--reload' if not config.isDeployed else ''}"
    )
    print(f"{' '*4}Server will be started with the command : {command}")
    return command








def add_middlewares(app: fastapi.FastAPI):
    from fastapi.middleware.cors import CORSMiddleware
    config_l = config.conf["SERVER_CORS"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config_l["AllowedDomains"],
        allow_credentials=True,
        allow_methods=config_l["AllowedMethods"],
        allow_headers=config_l["AllowedHeaders"],
    )







