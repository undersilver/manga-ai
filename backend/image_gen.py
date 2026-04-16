import replicate
import os

def generate_image(panel):
    try:
        # 👇 ここに入れる（この位置が重要）
        print("TOKEN:", os.getenv("REPLICATE_API_TOKEN"))

        output = replicate.run(
            "stability-ai/sdxl",
            input={
                "prompt": f"manga, black and white, {panel['scene']}",
                "width": 768,
                "height": 768
            }
        )
        return output[0]

    except Exception as e:
        print("IMAGE ERROR:", str(e))
        return "https://dummyimage.com/512x512/ff0000/ffffff&text=error"
