import os 
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.legacy.callbacks import CallbackManager
from llama_index.llms.openai_like import OpenAILike

os.environ['NLTK_DATA'] = '/root/llamaindex-demo/nltk_data'
load_dotenv()

base_url = "https://internlm-chat.intern-ai.org.cn/puyu/api/v1/"
api_key = os.environ["INTERNLM_API_KEY"]
model="internlm2.5-latest"

# Create an instance of CallbackManager
callback_manager = CallbackManager()

llm =OpenAILike(model=model, api_base=base_url, api_key=api_key, is_chat_model=True,callback_manager=callback_manager)

#初始化一个HuggingFaceEmbedding对象，用于将文本转换为向量表示
embed_model = HuggingFaceEmbedding(
#指定了一个预训练的sentence-transformer模型的路径
    model_name="/root/llamaindex-demo/model/sentence-transformer"
)
#将创建的嵌入模型赋值给全局设置的embed_model属性，
#这样在后续的索引构建过程中就会使用这个模型。
Settings.embed_model = embed_model

#初始化llm
Settings.llm = llm

#从指定目录读取所有文档，并加载数据到内存中
documents = SimpleDirectoryReader("/root/llamaindex-demo/data").load_data()
#创建一个VectorStoreIndex，并使用之前加载的文档来构建索引。
# 此索引将文档转换为向量，并存储这些向量以便于快速检索。
index = VectorStoreIndex.from_documents(documents)
# 创建一个查询引擎，这个引擎可以接收查询并返回相关文档的响应。
query_engine = index.as_query_engine()
response = query_engine.query("Python 3.13默认的dbm后端是什么模块？")

print(response)