import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

def extract():
    data = {}
    csv_files = list(RAW_DATA_PATH.glob("*.csv"))
    
    for file in csv_files:
        table_name = file.stem
        print(f"Loading {table_name}...")
        data[table_name] = pd.read_csv(file)
    
    print(f"\nExtract complete. {len(data)} tables loaded.")
    return data

if __name__ == "__main__":
    data = extract()
    for name, df in data.items():
        print(f"{name}: {df.shape[0]} rows, {df.shape[1]} columns")