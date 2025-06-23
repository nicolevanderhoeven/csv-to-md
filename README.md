# CSV to Markdown Converter

This is a Python script that converts a CSV file into individual Markdown files for each row in the CSV, for use in tools like Obsidian.

For example, if you have a CSV file with the following content:

```csv
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
```

After you run the script, it will create three Markdown files:
- `Alice.md`
- `Bob.md`
- `Charlie.md`

Each file will contain the data from the corresponding row in Markdown format. So `Alice.md` will look like this:

```markdown
---
name: Alice
age: 30
city: New York
---

# Alice


```

## Prerequisites
- Python 3.6 or later
- A CSV file with the data you want to convert

No third-party packages are required — only Python standard library modules (csv, os, re, and pathlib) are used.

## Usage

1. Locate your input CSV file and note its path (you can use the `inputfiles` folder already included, or create your own).
2. From the command line, navigate to the directory of this project.
3. Run the script with the paths to your input CSV file and the output directory where you want the Markdown files to be saved:

```bash
python csv_to_markdown.py inputfiles/yourfile.csv outputfiles
```

Change `inputfiles/yourfile.csv` to the path of your CSV file and `outputfiles` to the directory where you want the Markdown files to be saved.

After running the script, you will find the Markdown files in the specified output directory.