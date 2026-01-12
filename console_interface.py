# console_interface.py
# Membre 3 – Interface console SOC

import model_train
import pandas as pd

print("\n=== Interface SOC – Alert Scoring ===")

# تشغيل التدريب (كما هو)
# model_train.py يدرّب الموديل ويطبع النتائج
# ونستعمل df الموجود في نفس الجلسة
df = model_train.df if hasattr(model_train, "df") else None

# إذا df مش متاح (احتياط)
if df is None:
    print("[INFO] Les données sont générées depuis le module d'entraînement.")
    df = model_train.generate_alerts(500)

# إدخال Threshold
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


