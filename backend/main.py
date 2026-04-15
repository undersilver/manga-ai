from fastapi import FastAPI
from llm import split_into_panels
from image_gen import generate_image
from pdf import create_pdf

app = FastAPI()

@app.post("/generate")
async def generate(data: dict):
    novel = data["novel"]

    panels = split_into_panels(novel)

    images = []
    for panel in panels:
        img = generate_image(panel)
        images.append(img)

    pdf = create_pdf(images)

    return {"pdf": pdf}
