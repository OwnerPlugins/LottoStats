# -*- coding: utf-8 -*-
import json
import urllib.request
from .dati import save_superenalotto_archive

SUPERENALOTTO_URL = "https://raw.githubusercontent.com/Belfagor2005/Superenalotto/main/storico-estrazioni-superenalotto.json"


def download_and_convert_se():
    try:
        print("⬇️ Downloading Superenalotto archive from GitHub...")

        with urllib.request.urlopen(SUPERENALOTTO_URL) as response:
            json_data = response.read().decode('utf-8')

        data = json.loads(json_data)

        if isinstance(data, dict) and 'draws' in data:
            raw_draws = data['draws']
        else:
            raise Exception("Invalid JSON: missing 'draws' key")

        archive = []
        for idx, draw in enumerate(raw_draws):
            concorso = draw.get('concorso', idx + 1)

            archive.append({
                'data': draw['date'],
                'concorso': int(concorso),
                'numeri': sorted(draw['nums']),
                'jolly': draw.get('jolly'),
                'superstar': draw.get('ss')
            })

        save_superenalotto_archive(archive)
        print(f"✅ Superenalotto saved! {len(archive)} draws.")
        return True

    except Exception as e:
        print(f"❌ Superenalotto download error: {e}")
        import traceback
        traceback.print_exc()
        return False


def aggiorna_superenalotto():
    return download_and_convert_se()
