# -*- coding: utf-8 -*-
import random
from collections import defaultdict
from .dati import get_archive, FIXED_WHEELS


def calculate_frequencies():
    """Calculate frequencies of all numbers"""
    archive = get_archive()
    frequencies = defaultdict(int)

    for draw in archive:
        for wheel, numbers in draw['estrazioni'].items():
            for num in numbers:
                frequencies[num] += 1

    return dict(frequencies)


def calculate_delays():
    """Calculate delays of all numbers"""
    archive = get_archive()
    delays = {num: 0 for num in range(1, 91)}

    for num in range(1, 91):
        found = False
        for draw in reversed(archive):
            for wheel, numbers in draw['estrazioni'].items():
                if num in numbers:
                    found = True
                    break
            if found:
                break
            delays[num] += 1

    return delays


def get_full_analysis():
    """Complete statistical analysis"""
    archive = get_archive()
    frequencies = calculate_frequencies()
    delays = calculate_delays()

    # Most and least frequent
    most_frequent = max(frequencies.items(), key=lambda x: x[1])
    least_frequent = min(frequencies.items(), key=lambda x: x[1])

    # Max delay
    max_delay = max(delays.items(), key=lambda x: x[1])

    # Numbers per wheel
    numbers_per_wheel = defaultdict(list)
    for draw in archive:
        for wheel, numbers in draw['estrazioni'].items():
            numbers_per_wheel[wheel].extend(numbers)

    # Get top 5 per wheel
    for wheel in FIXED_WHEELS:
        if wheel in numbers_per_wheel:
            from collections import Counter
            counter = Counter(numbers_per_wheel[wheel])
            numbers_per_wheel[wheel] = [
                num for num, _ in counter.most_common(5)]

    return {
        'total_draws': len(archive),
        'most_frequent': most_frequent,
        'least_frequent': least_frequent,
        'max_delay': max_delay,
        'numbers_per_wheel': dict(numbers_per_wheel)
    }


def generate_predictions():
    """Generate statistical predictions"""
    frequencies = calculate_frequencies()
    delays = calculate_delays()

    # Combined score: frequency + delay weight
    scores = {}
    for num in range(1, 91):
        freq = frequencies.get(num, 0)
        delay = delays.get(num, 0)
        scores[num] = freq + (delay * 0.3)

    # Sort by score
    best = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    predictions = {}
    for wheel in FIXED_WHEELS:
        candidates = best[:20]
        chosen = random.sample(candidates, 5)
        predictions[wheel] = sorted([num for num, _ in chosen])

    return predictions


def get_dieci_lotto():
    """Get 10eLotto data"""
    archive = get_archive()
    frequencies = calculate_frequencies()

    # Simulate last 10eLotto draw (10 numbers)
    last = sorted(random.sample(range(1, 91), 10))

    return {
        'ultima': last,
        'frequenze': frequencies
    }
