# CS 789 — Assignment 4: What Actually Moves RAG Accuracy?

**UNLV · AI-Powered Cyber Attacks and Defenses · Fall 2026 · Prof. Yoohwan Kim**

One security corpus, one 26-question evaluation set, one fixed scorer — and you change one knob at a
time: chunking (fixed vs. recursive, 200 → 3200 characters), retrieval (BM25 vs. dense vs. hybrid),
the embedding model, the vector store (ChromaDB via LlamaIndex, Pinecone via LangChain), TurboQuant
vector compression, and finally the LLM's answers with the KV cache in bf16, fp8 and TurboQuant.

The handout is `CS 789 A4.docx` / `.pdf` on WebCampus. This README is the "how do I start" sheet.

## Start on Google Colab (recommended)

1. Open **https://colab.research.google.com/github/unlv-cs789-f26/A4/blob/main/A4_Vector_RAG.ipynb**
   (or in Colab: *File → Open notebook → GitHub* → `unlv-cs789-f26/A4`).
2. *Runtime → Change runtime type →* **L4 GPU** → *Save*. (A100 is fine too; T4 works for Parts A–D.)
3. *File → Save a copy in Drive* — otherwise your work disappears when the runtime ends.
4. Run cell 0.1. It clones this repo into `/content/A4`, installs the packages, and installs vLLM in the
   background for Part E.

## Start on your own computer

```bash
git clone https://github.com/unlv-cs789-f26/A4.git
cd A4
./start.sh            # makes .venv, installs, checks the machine, opens Jupyter Lab
./start.sh --vllm     # also installs vLLM for Part E (Linux/WSL2, NVIDIA GPU >= 16 GB)
./start.sh --check    # only the environment check
```

Windows: `start.bat` runs Parts A–D. Part E needs vLLM, which is Linux-only: use Colab or WSL2.

## Files

| file | what it is |
|---|---|
| `A4_Vector_RAG.ipynb` | the assignment notebook — 🛠️ build cells (with AI prompts), measure cells, ✍️ questions |
| `cs789rag.py` | the fixed harness: corpus loader, questions, metrics, results log, plots, vLLM helpers. **Do not edit.** |
| `corpus/` | 35 Vandelay Industries documents (fictional company, real ATT&CK technique ids) |
| `questions.yaml` | 26 questions with gold facts and gold documents, six question types |
| `PROMPTS.md` | how to use Claude in Chrome / Gemini in Chrome / Gemini in Colab, and prompt patterns |
| `install_vllm.sh` | installs vLLM into its own virtualenv (so it cannot break the notebook's PyTorch) |
| `requirements.txt` | notebook packages |
| `start.sh` / `start.bat` / `check_environment.py` | local start-up and checks |

Results you measure are appended to `results/results.jsonl`.

## Accounts you need

* Google account with **Colab Pro** (or free Colab Pro for verified US students).
* **Pinecone** free Starter account (Part D.2): app.pinecone.io → *API Keys*. Store the key in Colab 🔑
  Secrets as `PINECONE_API_KEY` — never in a code cell.
* An AI assistant in the browser: Claude in Chrome, Gemini in Chrome, or Gemini in Colab (see `PROMPTS.md`).

## Model downloads (automatic, from Hugging Face)

all-MiniLM-L6-v2 (90 MB), bge-base-en-v1.5 (440 MB), nomic-embed-text-v1.5 (550 MB), ATTACK-BERT
(440 MB), Qwen3-4B-Instruct-2507 (8 GB, served by vLLM in Part E).

## Submission

One PDF on WebCampus: the filled-in handout (tables, answers, AI-assistant log, screenshots) followed by
this notebook printed with its outputs (*File → Print → Save as PDF*).
