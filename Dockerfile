FROM huggingface/transformers-pytorch-gpu

RUN pip3 install -U transformers
RUN pip3 install jupyter

# Pre-download the weights for the models
# Tokenizer
RUN python3 -c "from transformers import AutoTokenizer;AutoTokenizer.from_pretrained('EleutherAI/gpt-j-6B')"
# Model - float16 (for inference)
RUN python3 -c "import torch;from transformers import AutoModelForCausalLM;AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-j-6B', revision='float16', torch_dtype=torch.float16, low_cpu_mem_usage=True)"
# Model - full precision
# RUN python -c "from transformers import AutoModelForCausalLM;AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-j-6B')"

COPY gptj.py gptj.py

