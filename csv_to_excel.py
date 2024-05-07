import pandas as pd

# Read the CSV file
df = pd.read_csv('book.csv')
# converted the CSV file to an Excel file
df.to_excel('output_book.xlsx', index=False)
