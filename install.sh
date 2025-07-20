#!/bin/bash

# Avbryt om något går fel
set -e

echo "🌀 Skapar virtuell miljö..."
python3 -m venv env

echo "⚙️  Aktiverar miljön..."
source env/bin/activate

echo "⬆️  Uppdaterar pip..."
pip install --upgrade pip

echo "📦 Installerar beroenden..."
pip install numpy==1.26.4 flask stanza

echo "🔥 Installerar CPU-version av PyTorch..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo "✅ Allt installerat. Nu laddar vi ner svenska modellen för Stanza..."
python3 -c "import stanza; stanza.download('sv')"

echo "🚀 Startar Flask-server..."
python3 app.py

