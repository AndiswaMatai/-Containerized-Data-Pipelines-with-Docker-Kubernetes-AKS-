import pandas as pd
import datetime

def extract():
    data = {
        "transaction_id": [1, 2, 3],
        "amount": [150.50, 220.00, 89.99],
        "currency": ["ZAR", "ZAR", "ZAR"],
        "timestamp": [datetime.datetime.now()] * 3
    }
    return pd.DataFrame(data)

def transform(df):
    df["amount_with_vat"] = df["amount"] * 1.15
    return df

def load(df):
    print("Final dataset:")
    print(df)

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
