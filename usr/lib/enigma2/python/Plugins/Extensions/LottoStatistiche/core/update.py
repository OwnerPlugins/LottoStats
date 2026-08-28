# -*- coding: utf-8 -*-
import os
import json
import urllib.request
import zipfile
import tempfile
from collections import defaultdict
from .dati import save_archive, DATA_FILE

ARCHIVE_URL = "https://www.brightstarlottery.it/STORICO_ESTRAZIONI_LOTTO/storico.zip"


def update_archive():
    """Download complete archive from brightstarlottery.it"""
    try:

        print("⬇️ Downloading complete archive from brightstarlottery.it...")

        with urllib.request.urlopen(ARCHIVE_URL) as response:
            zip_data = response.read()

        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp_zip:
            tmp_zip.write(zip_data)
            tmp_zip_path = tmp_zip.name

        draws_per_date = defaultdict(dict)

        with zipfile.ZipFile(tmp_zip_path, 'r') as zip_ref:

            txt_files = [f for f in zip_ref.namelist() if f.endswith('.txt')]
            if not txt_files:
                raise Exception("No .txt file found in ZIP")

            with zip_ref.open(txt_files[0]) as txt_file:
                for line in txt_file:
                    line = line.decode('utf-8', errors='ignore').strip()
                    if not line:
                        continue

                    parts = line.split()
                    if len(parts) < 7:
                        continue

                    raw_date = parts[0]      # 1939/01/07
                    wheel = parts[1]         # BA
                    numbers = [int(x) for x in parts[2:7]]

                    # Convert date to YYYY-MM-DD
                    date = raw_date.replace('/', '-')

                    draws_per_date[date][wheel] = numbers

        os.unlink(tmp_zip_path)

        # Build complete archive
        archive = []
        fixed_wheels = [
            'BA',
            'CA',
            'FI',
            'GE',
            'MI',
            'NA',
            'PA',
            'RM',
            'TO',
            'VE']

        for date in sorted(draws_per_date.keys()):
            draws = draws_per_date[date]
            complete_draws = {
                wheel: draws.get(
                    wheel, []) for wheel in fixed_wheels}

            archive.append({
                'data': date,
                'estrazioni': complete_draws
            })

        save_archive(archive)
        print(
            f"✅ Archive saved! {len(archive)} draws from {archive[0]['data']} to {archive[-1]['data']}")

        return True

    except Exception as e:
        print(f"❌ Download error: {e}")
        return False


def aggiorna_archivio():
    """Funzione chiamata dal plugin per aggiornare i dati"""
    # Controlla se l'archivio esiste già
    if os.path.exists(DATA_FILE):
        # Chiedi conferma
        # msg = "L'archivio esiste già. Vuoi aggiornarlo con i dati più recenti?"
        # Nota: in Enigma2 si usa MessageBox per chiedere conferma
        # Questo è un placeholder, va adattato alla tua interfaccia
        return update_archive()
    else:
        return update_archive()
