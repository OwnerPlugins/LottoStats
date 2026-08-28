# -*- coding: utf-8 -*-
import os
import json
import urllib.request
import csv
from .dati import save_superenalotto_archive

SUPERENALOTTO_URL = "https://raw.githubusercontent.com/luigimassa/superenalotto-archivio/refs/heads/main/superenalotto.csv"


def download_and_convert_se():
    """Download Superenalotto CSV and convert to JSON"""
    try:
        print("⬇️ Downloading Superenalotto archive...")
        
        with urllib.request.urlopen(SUPERENALOTTO_URL) as response:
            csv_data = response.read().decode('utf-8')
        
        lines = csv_data.strip().split('\n')
        reader = csv.DictReader(lines)
        
        archive = []
        for row in reader:
            date = row['data']
            contest = row['concorso']
            
            numbers = [
                int(row['n1']),
                int(row['n2']),
                int(row['n3']),
                int(row['n4']),
                int(row['n5']),
                int(row['n6'])
            ]
            
            jolly = int(row['jolly']) if row['jolly'] else None
            superstar = int(row['superstar']) if row['superstar'] else None
            
            archive.append({
                'data': date,
                'concorso': int(contest),
                'numeri': sorted(numbers),
                'jolly': jolly,
                'superstar': superstar
            })
        
        save_superenalotto_archive(archive)
        print(f"✅ Superenalotto saved! {len(archive)} draws.")
        return True
        
    except Exception as e:
        print(f"❌ Superenalotto download error: {e}")
        return False


def aggiorna_superenalotto():
    """Funzione chiamata dal plugin per aggiornare i dati"""
    # Controlla se esiste già un file di cache per non scaricare ogni volta
    CACHE_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'superenalotto_cache.json')
    
    # Se il file esiste e ha meno di 1 giorno, usalo
    if os.path.exists(CACHE_FILE):
        import time
        if time.time() - os.path.getmtime(CACHE_FILE) < 86400:  # 24 ore
            print("📂 Usando cache Superenalotto")
            return True
    
    # Altrimenti scarica
    return download_and_convert_se()
