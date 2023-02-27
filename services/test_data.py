import os
import pandas as pd


def get_data():
    try:
        data = pd.read_csv(os.path.join("data", "data.csv"), sep=",")
    except:
        print("Something went wrong. Could not get data")

    return data if not data.empty else None


def get_data_stats():
    data = get_data()

    if not data.empty:
        return data.shape
