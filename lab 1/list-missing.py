import pandas as pd

def list_columns_with_missing_values(input_file):
    # Đọc tập tin CSV
    df = pd.read_csv(input_file)

    # Tìm các cột có giá trị bị thiếu
    columns_with_missing_values = df.columns[df.isnull().any()].tolist()

    # In danh sách các cột có giá trị bị thiếu
    print("Columns with missing values:")
    for column in columns_with_missing_values:
        print(column)

if __name__ == '__main__':
    # Nhập tên tập tin CSV từ dòng lệnh
    input_file = input("Enter the name of the CSV file: ")

    # Gọi hàm liệt kê các cột có giá trị bị thiếu
    list_columns_with_missing_values(input_file)
