from app.utils import transcribe_audio, analyze_sentiment
from pathlib import Path

def main():
    audio_path = Path("audio") / "test.wav"

    if not audio_path.is_file():
        print(f"Erreur : le fichier audio '{audio_path}' n'existe pas.")
        return

    print("Lancement du test pipeline complet...")

    # Transcription
    print("Transcription en cours...")
    transcription = transcribe_audio(str(audio_path))
    print(f"Transcription : {transcription}")

    # Analyse de sentiment
    print("Analyse du sentiment...")
    sentiment = analyze_sentiment(transcription)
    print(f"Résultat sentiment : {sentiment}")

if __name__ == "__main__":
    main()
