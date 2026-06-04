import random

def get_signal_strength():
    return random.randint(1, 100)

def signal_status(strength):
    if strength < 30:
        return "Weak Signal"
    elif strength < 70:
        return "Medium Signal"
    else:
        return "Strong Signal"
