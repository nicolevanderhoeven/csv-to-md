import os
import csv
import re
import argparse

def safe_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', name)[:50]

def csv_to_markdown(input_csv, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with open(input_csv, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader, start=1):
            first_col = list(row.values())[0]
            safe_title = safe_filename(first_col) or f'row_{idx}'
            md_filename = os.path.join(output_dir, f'{safe_title}.md')

            with open(md_filename, 'w', encoding='utf-8') as md_file:
                md_file.write(f'---\n')
                for key, value in row.items():
                    md_file.write(f'{key}: {value}\n')
                md_file.write(f'---\n\n# {first_col}\n\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert CSV rows to Markdown files.")
    parser.add_argument('input_csv', help="Path to the input CSV file")
    parser.add_argument('output_dir', help="Directory where Markdown files will be saved")
    args = parser.parse_args()

    csv_to_markdown(args.input_csv, args.output_dir)
# Example usage:
# python scripts/create-md.py path/to/input.csv path/to/outputfilesfolder