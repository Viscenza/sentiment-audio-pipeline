from transformers import (
    Wav2Vec2ForCTC,
    Wav2Vec2Processor,
    pipeline,
    AutoTokenizer,
    AutoModelForSequenceClassification
)
import torch
import librosa

# === Chargement des modèles ===

# Pour la transcription audio
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
asr_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Pour l'analyse de sentiment
sentiment_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
sentiment_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Pipeline d'analyse de sentiment (transformers pipeline)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=sentiment_model,
    tokenizer=sentiment_tokenizer
)


# === Fonctions ===

def transcribe_audio(audio_path: str) -> str:
    """Convertit un fichier audio en texte via Wav2Vec2."""
    speech, sr = librosa.load(audio_path, sr=16000)  # Wav2Vec2 fonctionne mieux avec 16kHz
    input_values = processor(speech, return_tensors="pt", sampling_rate=16000).input_values

    with torch.no_grad():
        logits = asr_model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription.lower()


def analyze_sentiment(text: str) -> dict:
    """Analyse le sentiment d'un texte (positif/négatif/neutre)."""
    result = sentiment_pipeline(text)[0]
    return {"label": result['label'], "score": float(result['score'])}
