import replicate

def generate_image(panel):
    output = replicate.run(
        "stability-ai/sdxl",
        input={"prompt": panel["scene"]}
    )
    return output[0]
