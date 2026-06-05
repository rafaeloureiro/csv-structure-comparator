import pandas as pd


def compare_csv_structure(file1: str, file2: str):
    cols1 = list(pd.read_csv(file1, nrows=0).columns)
    cols2 = list(pd.read_csv(file2, nrows=0).columns)

    if cols1 == cols2:
        print("✅ Success: The CSV file structure is exactly the same.")
        return

    print("⚠️ Warning: Structural divergences were found!")

    missing_columns = set(cols1) - set(cols2)
    additional_columns = set(cols2) - set(cols1)

    if missing_columns:
        print(f"❌ Missing columns: {missing_columns}")

    if additional_columns:
        print(f"➕ Additional columns: {additional_columns}")

    if not missing_columns and not additional_columns:
        print("🔄 Same columns, different order.")
