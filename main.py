from fastapi import FastAPI, Request as req
from fastapi.responses import JSONResponse



app = FastAPI()


@app.post("/report")
async def respond_to_report(request:req):
   json_ = await req.json()
   print(json_)
   return JSONResponse({"success":True})

