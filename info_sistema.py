#!/usr/bin/env python3
import psutil
import shutil
from rich.console import Console
from rich.table import Table

def format_bytes(size):
    # Converte i byte in una stringa leggibile
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def main():
    console = Console()
    table = Table(title="--- Informazioni di Sistema ---")

    table.add_column("Parametro", justify="left", style="cyan", no_wrap=True)
    table.add_column("Valore", justify="right", style="magenta")

    # Uso CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    table.add_row("Uso CPU", f"{cpu_usage}%")
    
    # Uso RAM
    ram = psutil.virtual_memory()
    table.add_row("Uso RAM", f"{ram.percent}% (Disponibile: {format_bytes(ram.available)})")
    
    # Spazio Disco (root)
    usage = shutil.disk_usage("/")
    table.add_row("Spazio Disco Libero", f"{format_bytes(usage.free)} / {format_bytes(usage.total)}")

    console.print(table)

if __name__ == "__main__":
    main()
