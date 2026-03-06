import duckdb
from pathlib import Path

DB_PATH = "data/olist.duckdb"

def load(transformed_data):
    print(f"Loading data into DuckDB at {DB_PATH}...")
    
    Path("data").mkdir(exist_ok=True)
    con = duckdb.connect(DB_PATH)

    for table_name, df in transformed_data.items():
        print(f"Writing {table_name}...")
        con.execute(f"DROP TABLE IF EXISTS {table_name}")
        con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")

    con.close()
    print("\nLoad complete.")

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    data = extract()
    transformed = transform(data)
    load(transformed)