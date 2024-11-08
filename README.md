# TextSentinel

**TextSentinel** is a Python tool designed to help detect and highlight duplicate sentences in text files. It uses a simple GUI to let users select a file and then scans it to identify sentences that appear more than once, presenting the results in a structured, colorful table using the `rich` library.

## Features

- **File Selection**: Utilizes a file dialog for easy file selection.
- **Duplicate Detection**: Identifies sentences that repeat within the document, regardless of case or leading/trailing spaces.
- **Results Display**: Uses a table format with colors to present duplicate sentences, the number of repetitions, and their line numbers.
- **Colorful Output**: Leverages the `rich` library for an enhanced console output and `colorama` for cross-platform color support.

## Requirements

- Python 3.x
- Libraries: `tkinter`, `rich`, and `colorama`

You can install the required libraries via:
```bash
pip install rich colorama
```

## Usage

1. Run `textsentinel.py` using Python:
   ```bash
   python textsentinel.py
   ```
2. When prompted, select the text file you wish to scan.
3. If duplicate sentences are found, they will be displayed in a table showing:
   - **Sentence**: The repeated sentence.
   - **Number of Repetitions**: How many times it appears.
   - **Line Number**: The first occurrence of the sentence.

If no duplicates are found, a message will indicate this.

## Script Overview

- **Banner Display**: Displays a banner with gradient colors at the start.
- **File Selection**: Opens a file dialog for choosing a file to scan.
- **Duplicate Sentence Detection**: Scans the selected file, counting occurrences of each sentence.
- **Results Table**: Displays results with each duplicate sentence’s count and first appearance line number.
