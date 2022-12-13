# GPT-J Demo

This is just a super quick demo for `GPT-J` (included in the *Huggingface* `transformers` package) 
if anyone wants to try it out.

Not suitable for anything other then experimentation and demo.

Pay attention that this repo does not contain a lot of things including:
- Optimizations
- Error handlings

## Usage

```
# Build
docker-compose build

# Run
docker-compose up -d

# Then wait until each service is fully started (e.g.: GPT-J model needs to be loaded)
```

Then you can access the following:
- Swagger UI: `localhost:8008/docs`
- Streamlit App: `localhost:8050`

