# download_models.py

from transformers import (
    AutoModelForCTC,
    AutoProcessor,
    pipeline,
    AutoTokenizer,
    AutoModelForSequenceClassification
)
import os

# Crée le dossier models s’il n’existe pas
os.makedirs("models/wav2vec2-base-960h", exist_ok=True)
os.makedirs("models/distilbert-base-uncased-finetuned-sst-2-english", exist_ok=True)

print("⬇️ Téléchargement du modèle Wav2Vec2 (ASR)...")
AutoModelForCTC.from_pretrained(
    "facebook/wav2vec2-base-960h",
    cache_dir="./models/wav2vec2-base-960h"
)
AutoProcessor.from_pretrained(
    "facebook/wav2vec2-base-960h",
    cache_dir="./models/wav2vec2-base-960h"
)

print("✅ Wav2Vec2 téléchargé avec succès !\n")

print("⬇️ Téléchargement du modèle DistilBERT (sentiment)...")
AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    cache_dir="./models/distilbert-base-uncased-finetuned-sst-2-english"
)
AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    cache_dir="./models/distilbert-base-uncased-finetuned-sst-2-english"
)

print("✅ DistilBERT téléchargé avec succès !")
