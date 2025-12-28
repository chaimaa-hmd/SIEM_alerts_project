import random
import pandas as pd

def generate_alerts(n=500):
    sources = ['firewall', 'antivirus', 'IDS', 'system']
    users = ['admin', 'user1', 'user2']
    alerts = []
    for _ in range(n):
        alert = {
            'source': random.choice(sources),
            'user': random.choice(users),
            'freq': random.randint(1, 10),
            'criticite': round(random.random(), 2)
        }
        alerts.append(alert)
    return pd.DataFrame(alerts)


if __name__ == "__main__":
    df = generate_alerts()
    print(df.head())
