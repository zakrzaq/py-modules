from modules.greater import greet
from services.test_data import get_data, get_data_stats

greet()

data = get_data()

if not data.empty:
    print(data.head())
    print(get_data_stats())
