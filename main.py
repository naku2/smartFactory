from fastapi import FASTAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Template
from fastapi.staticfiles import StaticFiles
import shutil
import os

app = FASTAPI()

templates = Jinja2Template(directory="/Users/lee_seungkyu/Desktop/developer/HTML/")
app.mount("/static", StaticFiles(directory="/Users/lee_seungkyu/Desktop/developer/HTML/main.css", name="static"))
upload_folder = "/Users/lee_seungkyu/Desktop/developer/HTML/"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/predict", response_class=HTMLResponse)
async def read_predict(prediction_success: boll = True):
    return templates.TemplateResponse("predict.html", {"request": request, "prediction_success": prediction_success, "image_path": "/static/images/image_filename.jpg"})

@app.post("/uploadimage/")
async def upload_image(request: Request, image: UploadFile = File(...)):
    with open(os.path.join(upload_folder, image.filename), "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    prediction_success = True
    prediction_result = "Some Result"

    return templates.TemplateResponse("predict.html", {"request": request, "prediction_success": prediction_success, "prediction_result": prediction_result, "image_path": f"/static/images/{image.filename}"})


