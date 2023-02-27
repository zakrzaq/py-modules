from modules.greater import greet
from services.test_data import get_data

greet()

data = get_data()

if not data.empty:
    print(data.head())
