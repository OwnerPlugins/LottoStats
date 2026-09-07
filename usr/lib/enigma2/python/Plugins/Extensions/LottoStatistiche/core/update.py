# -*- coding: utf-8 -*-
import json
import urllib.request
from .dati import save_archive

ARCHIVE_URL = "https://raw.githubusercontent.com/Belfagor2005/ARCHIVIO-LOTTO/refs/heads/main/estrazioni.json"


def update_archive():
    """Download Lotto archive from GitHub and convert to plugin format"""
    try:
        print("⬇️ Downloading Lotto archive from GitHub...")

        with urllib.request.urlopen(ARCHIVE_URL) as response:
            json_data = response.read().decode('utf-8')

        data = json.loads(json_data)

        if not isinstance(data, list):
            raise Exception("Invalid JSON: expected list")

        archive = []
        for entry in data:
            # Convert data from dd/mm/yyyy a yyyy-mm-dd
            date_parts = entry['Data'].split('/')
            data_formatted = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"

            estrazioni = {}
            for ruota_data in entry['Ruote']:
                ruota = ruota_data['Ruota']
                # Mappa N1..N5 in una lista di int
                numeri = [
                    int(ruota_data['N1']),
                    int(ruota_data['N2']),
                    int(ruota_data['N3']),
                    int(ruota_data['N4']),
                    int(ruota_data['N5'])
                ]
                # Ordina i numeri come nel plugin
                estrazioni[ruota] = sorted(numeri)

            archive.append({
                'data': data_formatted,
                'estrazioni': estrazioni
            })

        save_archive(archive)
        print(
            f"✅ Lotto archive saved! {len(archive)} draws from {archive[0]['data']} to {archive[-1]['data']}")
        return True

    except Exception as e:
        print(f"❌ Lotto download error: {e}")
        import traceback
        traceback.print_exc()
        return False


def aggiorna_archivio():
    """Alias for update_archive"""
    return update_archive()
