#!/usr/bin/env python3
import psutil
import shutil

def format_bytes(size):
    # Converte i byte in una stringa leggibile
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def main():
    print("--- Informazioni di Sistema ---")
    
    # Uso CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Uso CPU: {cpu_usage}%")
    
    # Uso RAM
    ram = psutil.virtual_memory()
    print(f"Uso RAM: {ram.percent}% (Disponibile: {format_bytes(ram.available)})")
    
    # Spazio Disco (root)
    usage = shutil.disk_usage("/")
    print(f"Spazio Disco Libero: {format_bytes(usage.free)} / {format_bytes(usage.total)}")

if __name__ == "__main__":
    main()
