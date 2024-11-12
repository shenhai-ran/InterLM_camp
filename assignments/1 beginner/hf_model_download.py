# Load model directly
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "internlm/internlm2-chat-1_8b", trust_remote_code=True
)
