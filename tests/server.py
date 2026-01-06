import fastapi
import uvicorn
import sys
from fastapi.responses import FileResponse
from fastapi import Request, Header
from pathlib import Path

app = fastapi.FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# In-memory buffers (for demonstration)
file_buffers = {}


# Endpoint to serve the file
@app.get("/")
def read_root():
    file_path = sys.argv[1]
    print(f"Serving file: {file_path}")
    return FileResponse(file_path)


# Endpoint to receive chunks
@app.post("/receive")
async def receive_chunk(
    request: Request,
    x_file_name: str = Header(...),
    x_chunk_index: int = Header(...)
):

    chunk = await request.body()

    # Store in memory buffer
    if x_file_name not in file_buffers:
        file_buffers[x_file_name] = bytearray()
    file_buffers[x_file_name].extend(chunk)

    # Also append to disk
    file_path = UPLOAD_DIR / x_file_name
    with open(file_path, "ab") as f:
        f.write(chunk)

    return {"status": "ok", "chunk_index": x_chunk_index, "received_bytes": len(chunk)}


if __name__ == "__main__":
    import colorama
    colorama.init()
    uvicorn.run(app, host="0.0.0.0", port=8000)
