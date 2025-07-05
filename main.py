from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "VidGenAI API is running"}

@app.post("/generate-video/")
async def generate_video(image: UploadFile = File(...), description: str = ""):
    # Trả về video mẫu có thật
    return JSONResponse(content={
        "video_url": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4",
        "status": "success",
        "input_description": description
    })
