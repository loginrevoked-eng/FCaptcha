from fastapi import FastAPI, Request as req
from fastapi.responses import JSONResponse



app = FastAPI()


@app.post("/report")
async def respond_to_report(request:req):
   json_ = await request.json()
   print(json_)
   if html_content in globals:globals()["html_content"] += f"<pre>{json_}</pre>"
   else:globals()["html_content"] = f"<pre>{json_}</pre>"
   return JSONResponse({"success":True})

@app.get("/")
def root_():
    if globals().get("html_content",None) and html_content:
        return HTMLResponse(html_content)
    else:
        return HTMLResponse("<h1>Fuck you Mate</h1>") 