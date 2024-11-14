
# TextSentinel
![Banner](https://raw.githubusercontent.com/npcHamza/TextSentinel/refs/heads/main/banner.png)
**TextSentinel** is a Python tool designed to detect and highlight duplicate sentences in text files. Users can easily select a file directly from the current directory or via a file dialog. The tool then scans the file to identify sentences that appear more than once, presenting the results in a structured, colorful table using the `rich` library.

## Features
- **File Selection**: Lists compatible files (txt, json, jsonl, md) in the current directory. Users can either select from these files or use the file dialog to choose another.
- **Duplicate Detection**: Identifies sentences that repeat within the document, regardless of case or leading/trailing spaces.
- **Continuous Mode**: Allows users to scan multiple files in sequence without restarting the script. Pressing `q` exits the tool.
- **Results Display**: Uses a table format with colors to present duplicate sentences, the number of repetitions, and their line numbers.
- **Colorful Output**: Leverages the `rich` library for enhanced console output and `colorama` for cross-platform color support.

## Requirements
- **Python 3.x**
- **Libraries**: `rich` and `colorama`

Install required libraries with:
```bash
pip install rich colorama
```

## Usage
1. Run `textsentinel.py` using Python:
   ```bash
   python textsentinel.py
   ```
2. A list of compatible files in the current directory will be displayed, along with an option to open a file dialog for custom file selection.
3. Enter the number corresponding to the file you wish to scan. Pressing `q` will exit the tool.
4. If duplicate sentences are found, they will be displayed in a table with:
   - **Sentence**: The repeated sentence.
   - **Number of Repetitions**: How many times it appears.
   - **Line Number**: The first occurrence of the sentence.
5. If no duplicates are found, a message will indicate this.
6. After each file scan, the tool will reset, allowing users to select another file.

## Script Overview
- **Banner Display**: Displays a banner with gradient colors at the start.
- **File Selection**: Lists files in the current directory and includes an option to choose a file via file dialog.
- **Duplicate Sentence Detection**: Scans the selected file, counting occurrences of each sentence.
- **Results Table**: Displays results with each duplicate sentence’s count and first appearance line number.
