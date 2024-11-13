from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://internlm-chat.intern-ai.org.cn/puyu/api/v1/"
api_key = os.environ["INTERNLM_API_KEY"]
model="internlm2.5-latest"

# base_url = "https://api.siliconflow.cn/v1"
# api_key = "sk-请填写准确的 token！"
# model="internlm/internlm2_5-7b-chat"

client = OpenAI(
    api_key=api_key , 
    base_url=base_url,
)

chat_rsp = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Python 3.13默认的dbm后端是什么模块？"}],
)

for choice in chat_rsp.choices:
    print(choice.message.content)