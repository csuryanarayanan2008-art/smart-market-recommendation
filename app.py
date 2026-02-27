import os

file_path = os.path.join(os.path.dirname(__file__), "market_data.csv")
data = pd.read_csv(file_path)
