@echo off
REM CS 789 A4 - Windows start script.
REM Parts A-D run natively on Windows. Part E needs vLLM, which runs only on Linux:
REM use Google Colab (recommended) or WSL2 (then run ./start.sh --vllm inside WSL).
cd /d "%~dp0"
if not exist .venv python -m venv .venv
call .venv\Scripts\activate.bat
python -m pip -q install --upgrade pip
python -m pip -q install -r requirements.txt jupyterlab ipykernel matplotlib pandas
python check_environment.py
jupyter lab A4_Vector_RAG.ipynb
