import argparse
import pandas as pd

def list_columns_with_missing_values(input_file):
    df = pd.read_csv(input_file)
    columns_with_missing_values = df.columns[df.isnull().any()].tolist()
    print("Columns with missing values:")
    for column in columns_with_missing_values:
        print(column)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List columns with missing values in a CSV file.')
    parser.add_argument('input_file', help='Input CSV file')

    args = parser.parse_args()
    list_columns_with_missing_values(args.input_file)
