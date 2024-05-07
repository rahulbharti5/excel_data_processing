import pandas as pd
# Read Book data
input_file = 'book.xlsx'
output_file = 'output_book.xlsx'
df = pd.read_excel(input_file)
df['Title'] = df['Article'].str.split('\n').str[0]
df['Content'] = df['Article'].str.split('\n').str[1:].str.join('\n')
df.drop(columns=['Article'], inplace=True)
df = df[['Title', 'Content', 'Label']]
# Write the Datas to an Excel file again
df.to_excel(output_file, index=True)
