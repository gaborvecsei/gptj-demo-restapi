# GPT-J Demo

This is just a super quick demo for `GPT-J` (included in the *Huggingface* `transformers` package) 
if anyone wants to try it out.

Not suitable for anything other then experimentation and demo.

Pay attention that this repo does not contain:
- Optimizations
- Error handlings

## Usage

### Build Docker image

```
docker build -t gptj .
```

### Run

```
docker run -it --rm --name gptj --gpus '"device=7"' -p 8008:8008 --entrypoint /bin/bash gptj
```

Access the swagger ui at `localhost:8008/docs`

