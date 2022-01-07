# GPT-J for Inference

## Module usage
- (Build docker image)
- Run the docker image and start a notebook inside it `jupyter notebook --allow-root --port 9999 --ip 0.0.0.0`
- Import the `gptj` module and have fun

## RestAPI
`docker run -it --rm --name gptj --gpus '"device=7"' -p 8008:8008 --entrypoint /bin/bash gptj`

