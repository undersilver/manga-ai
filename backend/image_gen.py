import replicate
import time

def generate_image(panel):
    try:
        output = replicate.run(
            "black-forest-labs/flux-schnell",   # ← これが今一番安定
            input={
                "prompt": f"manga, black and white, {panel['scene']}"
            }
        )

        time.sleep(10)

        return output[0]

    except Exception as e:
        print("IMAGE ERROR:", str(e))
        return "https://dummyimage.com/512x512/ff0000/ffffff&text=error"
