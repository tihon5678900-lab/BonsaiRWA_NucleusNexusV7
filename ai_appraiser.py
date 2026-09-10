import os
from openai import OpenAI
import base64

NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")
client = OpenAI(api_key=NEBIUS_API_KEY, base_url="https://api.studio.nebius.com/v1/") if NEBIUS_API_KEY else None

def appraise_bonsai(image_file, species="Mai Vang"):
    if not client:
        return {"species":species,"style":"Truc Lac","age_years":27,"trunk_cm":18.5,"health_score":92,"rarity":87,"value_usd":18500,"value_vnd":470000000,"description_vn":"Mai Vang Thu Duc 27 nam, de nom dep","rwa_tier":"Gold","model":"Nebius Llama-3.1-405B demo","chain":"Base 8453"}
    img_bytes=image_file.getvalue()
    b64=base64.b64encode(img_bytes).decode()
    resp=client.chat.completions.create(model="meta-llama/Meta-Llama-3.1-405B-Instruct",messages=[{"role":"system","content":"You are bonsai appraiser. Return JSON"},{"role":"user","content":[{"type":"text","text":"Appraise bonsai"},{"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{b64}"}}]}],response_format={"type":"json_object"})
    import json
    data=json.loads(resp.choices[0].message.content)
    data["model"]="Nebius Llama-3.1-405B"; data["chain"]="Base 8453"
    return data