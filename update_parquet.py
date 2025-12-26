import pandas as pd

def generate_parquet():
    csv_file = 'tetralemma-reasoning-train.csv'
    parquet_file = 'tetralemma-reasoning-train.parquet'

    try:
        df = pd.read_csv(csv_file)
        print(f"Read {len(df)} rows from CSV.")

        # Verify columns
        if 'Question' not in df.columns or 'Reasoning' not in df.columns:
            raise ValueError("CSV missing required columns")

        df.to_parquet(parquet_file, engine='pyarrow')
        print(f"Successfully saved to {parquet_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_parquet()
