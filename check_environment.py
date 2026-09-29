"""CS 789 A4 environment check: python check_environment.py"""
import importlib, shutil, subprocess, sys
from pathlib import Path

ok = True
def line(name, good, detail=""):
    global ok
    ok &= bool(good)
    print(f"  [{'OK' if good else '!!'}] {name:28s} {detail}")

print("CS 789 A4 environment check")
line("python >= 3.10", sys.version_info >= (3, 10), sys.version.split()[0])
for mod in ["torch", "sentence_transformers", "rank_bm25", "turbovec", "chromadb", "llama_index.core",
            "langchain_text_splitters", "langchain_pinecone", "pinecone", "yaml", "pandas", "matplotlib"]:
    try:
        m = importlib.import_module(mod)
        line(mod, True, getattr(m, "__version__", ""))
    except Exception as e:
        line(mod, False, f"missing ({e.__class__.__name__}) -> pip install -r requirements.txt")
try:
    import torch
    cuda = torch.cuda.is_available()
    line("CUDA GPU", cuda, torch.cuda.get_device_name(0) if cuda else "no GPU: Parts A-D run on CPU (slower); Part E needs a GPU")
    if cuda:
        gb = torch.cuda.get_device_properties(0).total_memory / 2**30
        line("GPU memory >= 16 GB (Part E)", gb >= 15.5, f"{gb:.1f} GB")
except Exception:
    pass
here = Path(__file__).parent
line("corpus/ (35 docs)", len(list((here / "corpus").glob("*.md"))) == 35)
line("questions.yaml", (here / "questions.yaml").exists())
venv = Path("/content/vllm-env") if Path("/content").is_dir() else here / "vllm-env"
line("vLLM env (Part E)", (venv / "bin" / "vllm").exists(), str(venv) + ("" if (venv / "bin" / "vllm").exists() else "  -> bash install_vllm.sh"))
print("ALL GOOD" if ok else "Fix the [!!] lines above (Part E items can wait until Part E).")
