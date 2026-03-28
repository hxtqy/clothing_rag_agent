import streamlit as st
import time
from knowledge_base import KnowledgeBaseService


st.title("知识库更新服务")


if 'kb_service' not in st.session_state:
    st.session_state.kb_service = KnowledgeBaseService()

# file_uploader
uploader_file = st.file_uploader(
    label="请上传TXT文件",
    type=['txt'],
    accept_multiple_files=False,
    # False表示仅接受一个文件的上传
)

if uploader_file is not None:

    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024  # KB

    safe_file_name=file_name.replace("../","").replace("/","")
    #过滤 防止注入攻击
    st.subheader(f"文件名: {safe_file_name}")
    st.write(f"格式: {file_type} | 大小: {file_size:.2f} KB")

    # get_value -> bytes -> decode('utf-8')
    text = uploader_file.getvalue().decode("utf-8")

    # 显示文件内容预览
    with st.expander("文件内容预览"):
        st.text(text[:1000] + "..." if len(text) > 1000 else text)

    # 上传按钮
    if st.button("上传到知识库"):

        with st.spinner("正在处理文件..."):
            """渲染加载画面"""
            result = st.session_state.kb_service.upload_by_str(text, safe_file_name)
            st.success(result)