# Sentiment Audio Pipeline

Ce projet implémente un pipeline automatisé qui :

1. Transcrit un fichier audio vocal en texte (modèle Wav2Vec2)
2. Analyse le sentiment du texte (modèle NLP type BERT)
3. Propose une API FastAPI et une interface Gradio pour tester tout le pipeline
4. Peut être intégré à d'autres systèmes

## Structure du projet

sentiment-audio-pipeline/
│

├── app/

│ ├── main.py # API FastAPI

│ ├── model.py # Chargement des modèles

│ └── utils.py # Fonctions utilitaires

│

├── interface/

│ └── app_ui.py # Interface Gradio

│

├── audio/ # Dossier pour stocker des audios de test

├── models/ # (optionnel) Dossier de modèles ou config locale

├── README.md

├── requirements.txt

└── .gitignore

## Installation et exécution

### 1. Créer l’environnement virtuel

```bash
$ git clone https://github.com/Viscenza/sentiment-audio-pipeline.git
$ cd sentiment-audio-pipeline
$ python -m venv venv
```

### 2. Activer l'environnement
```bash 
$ venv\Scripts\activate  # (Windows)
$ source venv\source\activate # (UNIX)
```

### 3. Installer les dependances
```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
### 4. Lancer l'API FASTAPI
```bash
$ uvicorn app.main:app --reload
```

### 5. Lancer le gradio (depuis un autre terminal en activant venv)
```bash
$ python3 interface/app_ui.py
```
