import pandas as pd
from data_generator import generate_alerts

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


df = generate_alerts(500)

X = df.drop("criticite", axis=1)
y = df["criticite"]

cat_features = ["source", "user"]
num_features = ["freq"]

preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features),
        ("num", "passthrough", num_features)
    ]
)

model = RandomForestRegressor(random_state=42)

pipeline = Pipeline([
    ("preprocess", preprocess),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f"MAE du modèle : {mae:.3f}")

df["score_pred"] = pipeline.predict(X)

print(df.head())
