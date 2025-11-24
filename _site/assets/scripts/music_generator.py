#!/usr/bin/env python3
"""
Music Generator - Constrained Combinatorics Approach

Generates scales, melodies, and chord progressions using interval-based notation.
Based on the blog post "Music Theory as Constrained Combinatorics"
"""

import argparse
import random
from typing import List, Set, Tuple


# Constants
UNIVERSE = set(range(12))
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Common scales
SCALES = {
    'major': {0, 2, 4, 5, 7, 9, 11},
    'minor': {0, 2, 3, 5, 7, 8, 10},
    'dorian': {0, 2, 3, 5, 7, 9, 10},
    'phrygian': {0, 1, 3, 5, 7, 8, 10},
    'lydian': {0, 2, 4, 6, 7, 9, 11},
    'mixolydian': {0, 2, 4, 5, 7, 9, 10},
    'locrian': {0, 1, 3, 5, 6, 8, 10},
    'pentatonic_major': {0, 2, 4, 7, 9},
    'pentatonic_minor': {0, 3, 5, 7, 10},
}


def generate_constrained_scale(size: int = 7) -> Set[int]:
    """
    Generate a random scale following constraints:
    - Always includes 0 (root)
    - No more than 3 semitones between adjacent notes
    - Avoid consecutive 1-semitone or 3-semitone intervals

    Build by drawing intervals from a weighted distribution.
    Intervals: 1 (semitone), 2 (whole step), 3 (minor third)
    Weights: 1 is 3/14, 2 is 10/14, 3 is 1/14
    """
    scale = [0]  # Start with root
    current = 0
    last_interval = None

    while len(scale) < size:
        remaining = 12 - current
        valid_intervals = []
        weights = []

        # Interval 1: semitone (weight 3, no consecutive)
        if remaining > 1 and last_interval != 1:
            valid_intervals.append(1)
            weights.append(3)

        # Interval 2: whole step (weight 10, can repeat)
        if remaining > 2:
            valid_intervals.append(2)
            weights.append(10)

        # Interval 3: minor third (weight 1, no consecutive)
        if remaining > 3 and last_interval != 3:
            valid_intervals.append(3)
            weights.append(1)

        # No valid intervals means octave is filled
        if not valid_intervals:
            break

        # Weighted random selection (efficient, no list construction)
        interval = random.choices(valid_intervals, weights=weights, k=1)[0]

        current += interval
        scale.append(current)
        last_interval = interval

    return set(scale)


def get_stable_notes(scale: Set[int]) -> Set[int]:
    """
    Generate stable notes (typically root, third, fifth).
    Always includes 0 and 7 if available, plus one third.
    """
    stable = {0}

    # Add perfect fifth if in scale
    if 7 in scale:
        stable.add(7)
    elif 6 in scale:  # Diminished fifth fallback
        stable.add(6)
    elif 8 in scale:  # Augmented fifth fallback
        stable.add(8)

    # Add a third (prefer 3 or 4)
    if 4 in scale:  # Major third
        stable.add(4)
    elif 3 in scale:  # Minor third
        stable.add(3)

    return stable


def generate_melody(scale: Set[int], stable: Set[int], length: int = 16,
                    chord_progression: List[Set[int]] = None) -> List[int]:
    """
    Generate a melody following constraints:
    - Mostly stepwise or chord tone jumps
    - Avoids extreme leaps (> 7 semitones)
    - Ends on a stable tone
    - Range within 1-2 octaves
    """
    scale_list = sorted(list(scale))
    melody = []

    # Start on a stable note
    current = random.choice(list(stable))
    melody.append(current)

    # Track octave offset (0 = base, 12 = up octave, -12 = down octave)
    octave = 0

    for i in range(1, length):
        # Determine current chord if progression provided
        current_chord = None
        if chord_progression:
            chord_idx = (i // 4) % len(chord_progression)
            current_chord = chord_progression[chord_idx]

        # 60% chance of stepwise motion, 40% chance of leap
        if random.random() < 0.6:
            # Stepwise motion (1-2 semitones)
            direction = random.choice([-2, -1, 1, 2])
            next_note = (current + direction) % 12

            # Keep in scale
            if next_note not in scale:
                # Find nearest scale note
                distances = [(abs(next_note - s), s) for s in scale_list]
                next_note = min(distances)[1]

            # Update octave tracking
            if current + direction >= 12:
                octave += 12
            elif current + direction < 0:
                octave -= 12

        else:
            # Leap to chord tone or nearby scale note
            if current_chord and random.random() < 0.7:
                next_note = random.choice(list(current_chord))
            else:
                next_note = random.choice(scale_list)

        # Avoid going too high or low (keep within 2 octaves)
        if octave > 12:
            octave = 12
        elif octave < -12:
            octave = -12

        current = next_note
        melody.append(current + octave)

    # End on stable note (back to base octave)
    melody[-1] = random.choice(list(stable))

    return melody


def generate_chord_progression(scale: Set[int], length: int = 4) -> List[Set[int]]:
    """
    Generate a chord progression.
    Chords are built by stacking thirds from scale notes.
    """
    progression = []
    scale_list = sorted(list(scale))

    for _ in range(length):
        # Pick a root from the scale
        root = random.choice(scale_list)

        # Build triad by stacking thirds (3-4 semitones)
        chord = {root}
        current = root

        # Add third
        third_options = [(current + 3) % 12, (current + 4) % 12]
        third = next((t for t in third_options if t in scale), third_options[0])
        chord.add(third)

        # Add fifth
        fifth = (root + 7) % 12
        if fifth in scale:
            chord.add(fifth)
        else:
            # Try diminished or augmented fifth
            fifth_options = [(root + 6) % 12, (root + 8) % 12]
            fifth = next((f for f in fifth_options if f in scale), fifth_options[0])
            chord.add(fifth)

        # Sometimes add 7th
        if random.random() < 0.3 and len(scale) >= 7:
            seventh_options = [(root + 10) % 12, (root + 11) % 12]
            seventh = next((s for s in seventh_options if s in scale), None)
            if seventh:
                chord.add(seventh)

        progression.append(chord)

    return progression


def chord_to_guitar_tab(chord: Set[int], root_note: int = 0) -> Tuple[List[str], str]:
    """
    Convert a chord to a simple guitar tab voicing.
    Standard tuning: E(0), A(5), D(10), G(3), B(7), E(0)
    Returns (frets_list, compact_string)
    """
    # Transpose chord to actual pitches
    actual_pitches = {(p + root_note) % 12 for p in chord}

    # Standard tuning (in semitones from C), from low to high
    strings = [4, 9, 2, 7, 11, 4]  # E, A, D, G, B, E
    string_names = ['E', 'A', 'D', 'G', 'B', 'e']
    frets = []

    for string_pitch in strings:
        # Find closest chord tone within first 12 frets
        found = False
        for fret in range(13):
            if (string_pitch + fret) % 12 in actual_pitches:
                frets.append(str(fret))
                found = True
                break
        if not found:
            frets.append('x')

    return frets, string_names


def format_tab_vertical(frets: List[str], string_names: List[str]) -> str:
    """Format guitar tab in traditional vertical notation (high string on top)."""
    lines = []
    # Reverse to show high E on top
    for i in range(len(frets) - 1, -1, -1):
        fret = frets[i]
        string = string_names[i]
        # Pad fret values for alignment
        lines.append(f"{string}|--{fret.rjust(2)}--")
    return '\n      '.join(lines)


def format_note(pitch: int, root: int = 0) -> str:
    """Convert pitch class to note name."""
    return NOTE_NAMES[(pitch + root) % 12]


def format_set(notes: Set[int], root: int = 0) -> str:
    """Format a set of notes as intervals and names."""
    sorted_notes = sorted(list(notes))
    intervals = '{' + ', '.join(map(str, sorted_notes)) + '}'
    names = '{' + ', '.join(format_note(n, root) for n in sorted_notes) + '}'
    return f"{intervals} = {names}"


def main():
    parser = argparse.ArgumentParser(
        description='Generate music using constrained combinatorics',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--key', type=str, default=None,
                        help='Root note (C, D, E, F, G, A, B, with optional # or b)')
    parser.add_argument('--scale', type=str, default=None,
                        choices=list(SCALES.keys()),
                        help='Scale type (default: random or major)')
    parser.add_argument('--melody-length', type=int, default=16,
                        help='Number of notes in melody (default: 16)')
    parser.add_argument('--progression-length', type=int, default=4,
                        help='Number of chords in progression (default: 4)')
    parser.add_argument('--tabs', action='store_true',
                        help='Output guitar tabs for chord voicings')
    parser.add_argument('--random', action='store_true',
                        help='Generate completely random constrained scale')

    args = parser.parse_args()

    # Determine root note
    if args.key:
        key = args.key.upper().replace('B', 'b')
        if key.endswith('b') and len(key) == 2:
            # Flat: convert to sharp equivalent
            base = key[0]
            idx = (NOTE_NAMES.index(base) - 1) % 12
            root = idx
        else:
            try:
                root = NOTE_NAMES.index(key)
            except ValueError:
                print(f"Invalid key: {args.key}")
                return
    else:
        root = random.randint(0, 11)

    # Generate or select scale
    if args.random:
        scale = generate_constrained_scale()
        scale_name = 'random (constrained)'
    elif args.scale:
        scale = SCALES[args.scale]
        scale_name = args.scale
    else:
        scale = SCALES['major']
        scale_name = 'major'

    # Generate stable and color notes
    stable = get_stable_notes(scale)
    color = scale - stable

    # Generate chord progression
    progression = generate_chord_progression(scale, args.progression_length)

    # Generate melody
    melody = generate_melody(scale, stable, args.melody_length, progression)

    # Output
    print("=" * 60)
    print("MUSIC GENERATOR - Constrained Combinatorics")
    print("=" * 60)
    print()
    print(f"Key: {NOTE_NAMES[root]}")
    print(f"Scale: {scale_name}")
    print(f"  S = {format_set(scale, root)}")
    print()
    print("Stable Notes (T):")
    print(f"  T = {format_set(stable, root)}")
    print()
    print("Color Notes (C):")
    print(f"  C = {format_set(color, root)}")
    print()
    print(f"Chord Progression ({len(progression)} chords):")
    for i, chord in enumerate(progression, 1):
        print(f"  H{i} = {format_set(chord, root)}")
        if args.tabs:
            frets, string_names = chord_to_guitar_tab(chord, root)
            tab_display = format_tab_vertical(frets, string_names)
            print(f"      {tab_display}")
    print()
    print(f"Melody ({len(melody)} notes):")
    melody_notes = [format_note(m, root) for m in melody]
    # Print in groups of 8
    for i in range(0, len(melody_notes), 8):
        chunk = melody_notes[i:i+8]
        print(f"  {' - '.join(chunk)}")
    print()
    print("Melody (interval notation):")
    print(f"  M = [{', '.join(map(str, melody))}]")
    print()
    print("=" * 60)


if __name__ == '__main__':
    main()
