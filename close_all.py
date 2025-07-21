import os
import signal
import json

try:
    with open("processes.json", "r") as f:
        pids = json.load(f)

    for name, pid in pids.items():
        try:
            # Tuer tout le groupe de processus
            os.killpg(pid, signal.SIGTERM)
            print(f"Processus {name} (PID {pid}) arrêté.")
        except ProcessLookupError:
            print(f"Processus {name} (PID {pid}) déjà arrêté.")
        except PermissionError:
            print(f"Permission refusée pour tuer le processus {name} (PID {pid}).")
except FileNotFoundError:
    print("Fichier processes.json introuvable.")

