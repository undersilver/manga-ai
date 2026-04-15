from openai import OpenAI
import json

client = OpenAI()

def split_into_panels(novel):
    prompt = f"この文章を4コマ漫画にしてください：{novel}"

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(res.choices[0].message.content)
