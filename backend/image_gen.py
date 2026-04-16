import replicate
import time

def generate_image(panel):
    try:
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e5d6c6e5f5b3c9b1e5b6d8c5c1c7b7e8a9c0d1e2f3a4b5c6d7e8",  # ← 重要
            input={
                "prompt": f"manga, black and white, {panel['scene']}"
            }
        )

        time.sleep(10)

        return output[0]

    except Exception as e:
        print("IMAGE ERROR:", str(e))
        return "https://dummyimage.com/512x512/ff0000/ffffff&text=error"
