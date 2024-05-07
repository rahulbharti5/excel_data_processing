import csv

with open('book.csv', newline='') as input_file, open('refine_book.csv', 'w', newline='') as output_file:
    
    csvreader = csv.DictReader(input_file)
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(["Title", "Content", "Label"])
    
    for i, row in enumerate(csvreader):
            article_lines = row['Article'].split('\n')
            title = article_lines[0]  # First line is the title
            rest_of_article = '\n'.join(article_lines[1:])  # Rest of the lines form the article
            csvwriter.writerow([title, rest_of_article, row['Label']])
