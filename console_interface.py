# console_interface.py
# Interface console SOC

import model_train
import pandas as pd

print("\n=== Interface SOC – Alert Scoring ===")

# model_train.py
df = model_train.df if hasattr(model_train, "df") else None

if df is None:
    print("[INFO] Les données sont générées depuis le module d'entraînement.")
    df = model_train.generate_alerts(500)

# Threshold
threshold = float(input("Donner le seuil de criticité (0 à 1) : "))

# Filtrage + Tri
alertes_importantes = df[df["score_pred"] >= threshold]
alertes_importantes = alertes_importantes.sort_values(
    by="score_pred", ascending=False
)

print("\n⚠️ Alertes importantes (triées par criticité) :")

if alertes_importantes.empty:
    print("Aucune alerte au-dessus du seuil.")
else:
    print(alertes_importantes[["source", "user", "freq", "score_pred"]])


