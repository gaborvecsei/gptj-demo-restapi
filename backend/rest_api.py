import os
from typing import List, Optional

import fastapi
import gptj
import pydantic

app = fastapi.FastAPI()
app.gptj: Optional[gptj.GPTJ] = None


class GenerationResponse(pydantic.BaseModel):
    generated_text: str


class TokenIDResponse(pydantic.BaseModel):
    token_ids: List[int]


@app.get("/generate/", response_model=GenerationResponse)
async def generate(prompt: str,
                   temperature: float = 0.7,
                   max_token_length: int = 35,
                   eos_token_id: Optional[int] = None):
    generated_text: str = app.gptj.generate(prompt=prompt,
                                            temp=temperature,
                                            max_length=max_token_length,
                                            eos_token_id=eos_token_id)
    return GenerationResponse(generated_text=generated_text)


@app.get("/tokenize/", response_model=TokenIDResponse)
async def tokenize(prompt: str):
    token_ids = app.gptj.tokenize(prompt=prompt).flatten()
    token_ids = list(token_ids)
    return TokenIDResponse(token_ids=token_ids)


@app.on_event("startup")
async def startup():
    # Loading model which can take a minute or two
    app.gptj = gptj.GPTJ(device=gptj.get_device())


if __name__ == "__main__":
    REST_API_HOST = os.environ.get("REST_API_HOST", None)
    REST_API_PORT = os.environ.get("REST_API_PORT", None)
    if REST_API_HOST is None or REST_API_PORT is None:
        raise RuntimeError("These env variables should be present")
    import uvicorn
    uvicorn.run(app, host=REST_API_HOST, port=str(REST_API_PORT))
