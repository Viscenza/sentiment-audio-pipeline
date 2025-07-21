from transformers import pipeline

# Chargement du pipeline de transcription vocale
transcription_pipeline = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

# Chargement du pipeline d'analyse de sentiment
sentiment_pipeline = pipeline("sentiment-analysis")
