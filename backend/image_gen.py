import replicate
import time

def generate_image(panel):
    try:
        output = replicate.run(
            "stability-ai/sdxl",
            input={
                "prompt": f"manga, black and white, {panel['scene']}",
                "width": 768,
                "height": 768
            }
        )

        time.sleep(10)  # ← 超重要（制限回避）

        return output[0]

    except Exception as e:
        print("IMAGE ERROR:", str(e))
        return "https://dummyimage.com/512x512/ff0000/ffffff&text=error"
