md5_path = "./md5.text"

# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"

# 会话历史存储路径
chat_history_path = "./chat_history"

# splitter
chunk_size = 1000
chunk_overlap = 100
separators = [
    "\n\n",
    "\n",
    "。",
    "！",
    "？",
    ". ",
    "! ",
    "? ",
    ".",
    "!",
    "?",
    " ",
    "" ,
]

# 检索返回匹配的文档数量
similarity_threshold = 2

# 模型配置
embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"