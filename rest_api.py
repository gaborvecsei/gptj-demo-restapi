from typing import Optional, List

import fastapi
import pydantic

import gptj

app = fastapi.FastAPI()
print("Loading model...")
app.gptj = gptj.GPTJ(device=gptj.get_device())
print("Model loaded")


class GenerationRequest(pydantic.BaseModel):
    prompt: str
    temperature: float = 0.7
    max_token_length: int = 35
    eos_token_id: Optional[int] = None


class GenerationResponse(pydantic.BaseModel):
    generated_text: str


class TokenIDResponse(pydantic.BaseModel):
    token_ids: List[int]


@app.post("/generate/", response_model=GenerationResponse)
async def generate(generation_request: GenerationRequest):
    generated_text: str = app.gptj.generate(prompt=generation_request.prompt,
                                            temp=generation_request.temperature,
                                            max_length=generation_request.max_token_length,
                                            eos_token_id=generation_request.eos_token_id)
    return GenerationResponse(generated_text=generated_text)


@app.get("/tokenize/", response_model=TokenIDResponse)
async def tokenize(prompt: str):
    token_ids = app.gptj.tokenize(prompt=prompt)
    print(token_ids, type(token_ids), type(token_ids[0]))
    token_ids = list(token_ids)
    return TokenIDResponse(token_ids=token_ids)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)
