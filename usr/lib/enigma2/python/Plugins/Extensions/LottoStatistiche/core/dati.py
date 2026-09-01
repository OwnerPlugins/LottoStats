# -*- coding: utf-8 -*-
import json
import os
import random
from datetime import datetime, timedelta

DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    '..',
    'data',
    'archivio.json')
DATA_FILE_SE = os.path.join(
    os.path.dirname(__file__),
    '..',
    'data',
    'superenalotto.json')

FIXED_WHEELS = ['BA', 'CA', 'FI', 'GE', 'MI', 'NA', 'PA', 'RM', 'TO', 'VE']


def get_archive():
    """Return the complete draws archive"""
    if not os.path.exists(DATA_FILE):
        from .update import update_archive
        if not update_archive():
            return generate_fake_archive()

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_archivio():
    """Alias for get_archive (backward compatibility)"""
    return get_archive()


def save_archive(archive):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(archive, f, indent=2, ensure_ascii=False)


def get_superenalotto_archive():
    """Return the Superenalotto archive"""
    if not os.path.exists(DATA_FILE_SE):
        from .update_superenalotto import download_and_convert_se
        if not download_and_convert_se():
            return generate_fake_se_archive()

    with open(DATA_FILE_SE, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_archivio_se():
    """Alias for get_superenalotto_archive (backward compatibility)"""
    return get_superenalotto_archive()


def save_superenalotto_archive(archive):
    os.makedirs(os.path.dirname(DATA_FILE_SE), exist_ok=True)
    with open(DATA_FILE_SE, 'w', encoding='utf-8') as f:
        json.dump(archive, f, indent=2, ensure_ascii=False)


def generate_fake_archive():
    """Generate fake archive for testing"""
    archive = []
    base_date = datetime.now() - timedelta(days=365 * 2)

    for i in range(200):
        date = (base_date + timedelta(days=i * 2)).strftime('%Y-%m-%d')
        draws = {}
        for wheel in FIXED_WHEELS:
            numbers = sorted(random.sample(range(1, 91), 5))
            draws[wheel] = numbers
        archive.append({
            'data': date,
            'estrazioni': draws
        })

    save_archive(archive)
    return archive


def generate_fake_se_archive():
    """Generate fake Superenalotto archive for testing"""
    archive = []
    for i in range(100):
        numbers = sorted(random.sample(range(1, 91), 6))
        archive.append({
            'data': f'2024-01-{(i + 1):02d}',
            'concorso': i + 1,
            'numeri': numbers,
            'jolly': random.randint(1, 90),
            'superstar': random.randint(1, 90)
        })
    save_superenalotto_archive(archive)
    return archive
