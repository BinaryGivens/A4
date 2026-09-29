#!/usr/bin/env bash
# CS 789 A4 — start script for your OWN computer (Linux, macOS, or Windows via WSL2).
# On Google Colab you do not need this: open A4_Vector_RAG.ipynb from GitHub in Colab instead.
#
#   ./start.sh            create .venv, install packages, check the machine, open Jupyter Lab
#   ./start.sh --vllm     also install vLLM (Part E; needs an NVIDIA GPU with >= 16 GB)
#   ./start.sh --check    only run the environment check
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
if [ "$1" = "--check" ]; then $PY check_environment.py; exit 0; fi
if [ ! -d .venv ]; then
  echo "== creating .venv"; $PY -m venv .venv
fi
. .venv/bin/activate
python -m pip -q install --upgrade pip
echo "== installing packages (first time: a few minutes)"
python -m pip -q install -r requirements.txt jupyterlab ipykernel matplotlib pandas
if [ "$1" = "--vllm" ]; then bash install_vllm.sh; fi
python check_environment.py || true
echo "== opening Jupyter Lab: open A4_Vector_RAG.ipynb"
exec jupyter lab A4_Vector_RAG.ipynb
