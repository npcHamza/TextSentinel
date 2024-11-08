import tkinter as tk
from tkinter import filedialog
from collections import Counter
from rich.console import Console
from rich.table import Table

from colorama import init

init(autoreset=True)

console = Console()
banner_text = ["""
__ __|             |     ___|                |   _)               |
   |   _ \ \ \  /  __| \___ \    _ \  __ \   __|  |  __ \    _ \  |
   |   __/  `  <   |         |   __/  |   |  |    |  |   |   __/  |
  _| \___|  _/\_\ \__| _____/  \___| _|  _| \__| _| _|  _| \___| _|
  
  /HFerrahoglu
"""]

colors = ["yellow"]

def print_gradient_banner():
    console.print("") 
    for line, color in zip(banner_text, colors):
        console.print(f"[{color}]{line}[/]")


def select_file():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(title="Bir dosya seçin")  
    return file_path

def find_duplicate_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sentence_counts = Counter()
    sentence_lines = {}

    for line_num, line in enumerate(lines, start=1):
        sentences = line.split('.')
        for sentence in sentences:
            sentence = sentence.strip().lower()
            if sentence:
                sentence_counts[sentence] += 1
                if sentence_counts[sentence] == 1:
                    sentence_lines[sentence] = line_num
    
    duplicates = {sentence: (count, sentence_lines[sentence]) for sentence, count in sentence_counts.items() if count > 1}
    
    return duplicates

print_gradient_banner()
file_path = select_file()

if file_path:
    duplicates = find_duplicate_sentences(file_path)

    if duplicates:
        table = Table(title=" ", style="bold cyan")
        table.add_column("Sentence", style="bold red", width=50)
        table.add_column("Number of Repetitions", justify="center", style="bold green")
        table.add_column("Line Number", justify="center", style="bold yellow")
        
        for sentence, (count, line_num) in duplicates.items():
            table.add_row(sentence, str(count), str(line_num))
        
        console.print(table)
    else:
        console.print("[bold green]Repeating sentence not found.[/bold green]")
else:
    console.print("[bold red]Invalid file selected or no file selected![/bold red]")
