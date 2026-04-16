from fastapi import FastAPI
from backend.llm import split_into_panels
from backend.image_gen import generate_image

app = FastAPI()

@app.post("/generate")
async def generate(data: dict):
    novel = data["novel"]

    panels = split_into_panels(novel)

    images = []
    for panel in panels:
        img = generate_image(panel)
        images.append(img)

    return {"images": images}   # ← ここ修正
