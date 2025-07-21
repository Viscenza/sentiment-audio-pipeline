# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import JSONResponse
# import uvicorn
# import os
# from app.utils import transcribe_audio, analyze_sentiment

# app = FastAPI(
#     title="Sentiment Audio API",
#     description="API pour transcrire un fichier audio et analyser le sentiment",
#     version="1.0.0"
# )

# @app.post("/analyze/")
# async def analyze_audio(file: UploadFile = File(...)):
#     try:
#         # Sauvegarde temporaire du fichier
#         temp_path = f"temp_{file.filename}"
#         with open(temp_path, "wb") as f:
#             f.write(await file.read())

#         # Transcription et analyse de sentiment
#         transcription = transcribe_audio(temp_path)
#         sentiment = analyze_sentiment(transcription)

#         # Nettoyage
#         os.remove(temp_path)

#         return JSONResponse({
#             "transcription": transcription,
#             "sentiment": {
#                 "label": sentiment.get("label", "N/A"),
#                 "score": round(sentiment.get("score", 0), 2)
#             }
#         })

#     except Exception as e:
#         return JSONResponse({"error": str(e)}, status_code=500)

# if __name__ == "__main__":
#     uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
#test


# app/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import shutil
from app.utils import transcribe_audio, analyze_sentiment

app = FastAPI()

# Pour permettre à Gradio d'appeler l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API de transcription et analyse de sentiment"}

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    print("/n ON TEST /n")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    transcription = transcribe_audio(tmp_path)
    sentiment = analyze_sentiment(transcription)
    return {"transcription": transcription, "sentiment": sentiment}
