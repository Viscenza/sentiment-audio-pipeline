import subprocess
import json

# Lancer Gradio dans un terminal
p1 = subprocess.Popen(["python", "interface/app_ui.py"])

# Lancer FastAPI dans un autre
p2 = subprocess.Popen(["uvicorn", "app.main:app", "--port", "4500", "--reload"])


with open("processes.json", "w") as f:
    json.dump({"app_ui_pid": p1.pid, "fastapi_pid": p2.pid}, f)

print("Les processus sont lancés.")
