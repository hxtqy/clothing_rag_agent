from huggingface_hub import snapshot_download
import os

snapshot_download(
    repo_id="Qwen/Qwen3.5-9B",
    local_dir="D:/wast/Qwen3.5-9B",
    local_dir_use_symlinks=False,
    resume_download=True,
    max_workers=8
)