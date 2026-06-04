from datetime import datetime

def log_data(strength, status):
    with open("log.txt", "a") as file:
        file.write(f"{datetime.now()} - Strength: {strength} - Status: {status}\n")
