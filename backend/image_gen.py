import replicate
import time

def generate_image(panel):
    try:
        output = replicate.run(
            "lucataco/sdxl",   # ← ここ変更（これが今使える）
            input={
                "prompt": f"manga, black and white, {panel['scene']}"
            }
        )

        time.sleep(10)

        return output[0]

    except Exception as e:
        print("IMAGE ERROR:", str(e))
        return "https://dummyimage.com/512x512/ff0000/ffffff&text=error"
