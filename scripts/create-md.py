import os
import csv
import re

dir = '/Users/nic/git/md-from-csv/'
filename = os.path.join(dir, 'inputfiles/input.csv')
output_dir = os.path.join(dir, 'outputfiles')
os.makedirs(output_dir, exist_ok=True)

def safe_filename(name):
    # Remove unsafe characters and limit length
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', name)[:50]

with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for idx, row in enumerate(csvreader, start=1):
        first_column_value = list(row.values())[0]
        safe_title = safe_filename(first_column_value) or f'row_{idx}'
        md_filename = os.path.join(output_dir, f'{safe_title}.md')

        with open(md_filename, mode='w', encoding='utf-8') as md_file:
            md_file.write(f'---\n')
            for key, value in row.items():
                md_file.write(f'{key}: {value}\n')
            md_file.write(f'---\n\n# {first_column_value}\n\n')
