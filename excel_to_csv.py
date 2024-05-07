import pandas as pd
df = pd.read_excel('book.xlsx')
# convertedfrom excel to csv
df.to_csv('output_book.csv', index=False)
