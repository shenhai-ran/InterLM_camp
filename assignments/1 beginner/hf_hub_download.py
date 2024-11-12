from huggingface_hub import snapshot_download

local_dir = "/downloads/"
snapshot_download(
    repo_id="internlm/internlm2-chat-1_8b", allow_patterns="*.json", local_dir=local_dir
)
