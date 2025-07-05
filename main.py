from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "VidGenAI API is running"}

@app.post("/generate-video/")
async def generate_video(image: UploadFile = File(...), description: str = ""):
    # Mô phỏng phản hồi (vì chưa tích hợp AI thật)
    return JSONResponse(content={
        "video_url": "https://your-video-hosting.com/sample.mp4",
        "status": "success",
        "input_description": description
    })
