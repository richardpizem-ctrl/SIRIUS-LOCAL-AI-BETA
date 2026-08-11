# AUTONOMY TEST INPUT – SIMULÁCIA RASTU CPU
# Tento modul NENARÚŠA monitor.py

simulated_cpu = 16.0

def snapshot():
    global simulated_cpu

    # CPU rastie v každom cykle o 6 %
    simulated_cpu += 6.0
    if simulated_cpu > 95:
        simulated_cpu = 16.0  # reset po dosiahnutí maxima

    return {
        "system": {
            "cpu": round(simulated_cpu, 1),
            "ram": 43.0,
            "disk": 41.0
        }
    }
