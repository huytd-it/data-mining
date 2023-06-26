import argparse
import pandas as pd

def impute_missing_values(input_file, method, columns, output_file):
    df = pd.read_csv(input_file)

    for column in columns:
        if method == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif method == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif method == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)

    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Impute missing values in a CSV file.')
    parser.add_argument('input_file', help='Input CSV file')
    parser.add_argument('--method', choices=['mean', 'median', 'mode'], default='mean', help='Imputation method')
    parser.add_argument('--columns', nargs='+', help='Columns to impute')
    parser.add_argument('--out', dest='output_file', help='Output CSV file')

    args = parser.parse_args()
    impute_missing_values(args.input_file, args.method, args.columns, args.output_file)
