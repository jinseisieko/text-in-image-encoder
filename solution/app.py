import io

from PIL import Image, ImageDraw
from fastapi import FastAPI
from pydantic import BaseModel
import base64

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


class EncodeRequest(BaseModel):
    text: str


class EncodeResponse(BaseModel):
    data: str  # base64 image


class DecodeRequest(BaseModel):
    data: str  # base64 image


class DecodeResponse(BaseModel):
    text: str


def read_text_from_image(image_bytes: bytes) -> str:
    return "Decoded text (mocked)"


@app.post("/encode", response_model=EncodeResponse)
async def encode_text(request: EncodeRequest):
    image = Image.new("RGB", (200, 200), "black")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    
    return EncodeResponse(data=image_base64)


@app.post("/decode", response_model=DecodeResponse)
async def decode_image(request: DecodeRequest):
    image_bytes = base64.b64decode(request.data)
    text = read_text_from_image(image_bytes)
    return DecodeResponse(text=text)



@app.get("/ping")
async def ping():
    return 'ok'

