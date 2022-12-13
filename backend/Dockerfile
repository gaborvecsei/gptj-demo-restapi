FROM pytorch/pytorch:1.9.1-cuda11.1-cudnn8-runtime

RUN pip3 install -U transformers
RUN pip3 install accelerate

# Pre-download the weights for the models (because of this the docler image will be quite big)
# Tokenizer
RUN python3 -c "from transformers import AutoTokenizer;AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B')"
# Model - float16 (for inference)
RUN python3 -c "import torch;from transformers import AutoModelForCausalLM;AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-j-6B', revision='float16', torch_dtype=torch.float16, low_cpu_mem_usage=True)"
# Model - full precision
# RUN python -c "from transformers import AutoModelForCausalLM;AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-j-6B')"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /workspace

COPY gptj.py gptj.py
COPY rest_api.py rest_api.py

