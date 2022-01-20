from typing import Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def is_gpu_available():
    return torch.cuda.is_available()


def get_device():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    return device


class GPTJ:

    def __init__(self, device: str = "cpu") -> None:
        self.device = device
        self.model = None
        self.tokenizer = None
        self.load()

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
        self.model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B",
                                                          revision="float16",
                                                          torch_dtype=torch.float16,
                                                          low_cpu_mem_usage=True)
        self.model = self.model.to(self.device)

    def tokenize(self, prompt: str):
        input_ids = self.tokenizer(prompt, return_tensors="pt").to(self.device).input_ids
        return input_ids

    def generate(self, prompt: str, temp: float = 0.7, max_length: int = 20, eos_token_id: Optional[int] = None) -> str:
        input_ids = self.tokenize(prompt)
        gen_tokens = self.model.generate(input_ids,
                                         do_sample=True,
                                         temperature=temp,
                                         max_length=max_length,
                                         eos_token_id=eos_token_id)
        gen_text = self.tokenizer.batch_decode(gen_tokens)[0]
        return gen_text
