from fastapi import FastAPI, UploadFile, File, Request as req, Response
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn
import os
import aiofiles
import colorama

app = FastAPI()
html_content = ""
env = os.environ
uploaded_file_names = {}
PORT = int(env["PORT"])
HOSTNAME = f'{env["HOST"]}:{PORT}' if env.get("DEV",None) else "fcaptcha.onrender.com"

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = (await file.read()).decode("utf-8")
    except UnicodeDecodeError:
        return JSONResponse({"msg":"Nigga we only accept text files through this route"})
    saved_file_name = f"mulpar_{file.filename}"

    async with aiofiles.open(saved_file_name, "w") as f:
        await f.write(content)

    uploaded_file_names[file.filename] = saved_file_name
    return JSONResponse({"msg": f"file saved to {saved_file_name}"})

@app.get("/see_file_list")
def get_file_list():
    return JSONResponse(content=globals()["uploaded_file_names"])

@app.get("/see_files_uploaded/{f_name}")
def serve_file(f_name: str):
    # Check if the alias exists in your globals
    real_filename = globals()["uploaded_file_names"].get(f_name)

    if real_filename:
        file_path = os.path.join(os.getcwd(), real_filename)
        with open(file_path, "r") as f:
            return Response(content=f.read(), media_type="text/plain")

    # Fallback if file not found
    api_list_url = f"https://{HOSTNAME}/see_file_list"
    return Response(
        content=f"File not found. Visit {api_list_url} for valid names.",
        media_type="text/plain"
    )


@app.post("/report")
async def respond_to_report(request:req):
   json_ = await request.json()
   print(json_)
   global html_content
   html_content += f"<pre>{json_}</pre>"
   return JSONResponse({"success":True})

@app.get("/")
def root_():
    if html_content:
        return HTMLResponse(html_content)
    else:
        return HTMLResponse("<h1>Fuck you Mate</h1>")




def run_uvicorn_from_inside():
    colorama.init()
    uvicorn.run(
        app=app,
        host=env.get("HOST", "0.0.0.0"),
        port=PORT
    )

def get_filename(f_path:str):
    if "/" in f_path:
        return f_path.split('/')[-1].replace(".py", "")
    else:
        return f_path.split('\\')[-1].replace(".py", "")


if __name__ == "__main__":
    if env.get("DEV", None):
        run_uvicorn_from_inside()
    else:
        print(f"Run with uvicorn {get_filename(__file__)}:app --port [{PORT}] --host [{HOST}]")
