import pandas as pd

def count_rows_with_missing_values(input_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Count the number of rows with missing values
    num_rows_with_missing_values = df.isnull().any(axis=1).sum()

    # Print the result
    print("Number of rows with missing values:", num_rows_with_missing_values)

if __name__ == '__main__':
    # Enter the name of the CSV file
    input_file = input("Enter the name of the CSV file: ")

    # Call the function to count rows with missing values
    count_rows_with_missing_values(input_file)
