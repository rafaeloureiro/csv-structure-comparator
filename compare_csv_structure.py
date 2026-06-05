import pandas as pd


def compare_csv_structure(file1: str, file2: str):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    if set(df1.columns) == set(df2.columns):
        print("✅ Success: The CSV file structure is exactly the same.")
    else:
        print("⚠️  Warning: Structural divergences were found!\n")

        missing_columns = set(df1.columns) - set(df2.columns)
        additional_columns = set(df2.columns) - set(df1.columns)

        if missing_columns:
            print(f"❌ Columns missing in the new file: {missing_columns}")

        if additional_columns:
            print(f"➕ New columns that were added: {additional_columns}")


if __name__ == "__main__":
    compare_csv_structure("data/dados_modelo.csv", "data/dados_recebidos.csv")
