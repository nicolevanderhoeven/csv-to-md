import os
import csv

dir='/Users/nic/git/md-from-csv/'
filename = dir + 'inputfiles/input.csv'

if not os.path.exists(dir + '/outputfiles'):
    os.makedirs(dir + '/outputfiles')

outputFilePath = dir + 'outputfiles/'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for idx, row in enumerate(reader, start=1):
            md_filename = os.path.join(outputFilePath, f'row_{idx}.md')
            with open(md_filename, mode='w', encoding='utf-8') as md_file:
                md_file.write(f'# Row {idx}\n\n')
                for key, value in row.items():
                    md_file.write(f'{key}: {value}\n\n')