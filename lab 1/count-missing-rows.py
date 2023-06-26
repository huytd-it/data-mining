import argparse
import pandas as pd

def count_rows_with_missing_values(input_file):
    df = pd.read_csv(input_file)
    num_rows_with_missing_values = df.isnull().any(axis=1).sum()
    print("Number of rows with missing values:", num_rows_with_missing_values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count the number of rows with missing values in a CSV file.')
    parser.add_argument('input_file', help='Input CSV file')

    args = parser.parse_args()
    count_rows_with_missing_values(args.input_file)
