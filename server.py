from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
import json
import model

#model = load_model('classifier1.h5')
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    temp_file = _save_file_to_disk(image, path="temp", save_as="temp")
    tempr=random.randint(50,101)
    fire = model.predict(temp_file)
    print(fire)
    if fire:
        if tempr>70: 
            prediction = 'fire'           
        else:
            prediction = 'fire and smoke'
    else:
        prediction = 'no fire'

    return 
    return {"filename": image.filename, "prediction": prediction}
