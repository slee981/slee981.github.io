---
title: Music Theory as Constrained Combinatorics
layout: post
categories: [Music, Math]
tags: [music-theory, intervals, jazz, modeling]
katex: true
---

## Introduction

When I first tried to learn about music, the vocabulary didn't make much sense to me. Specifically, the system of letters with arbtrary seeming full and half steps between them was hard for me to remember and memorize. What do you mean there's no "C-flat"?  

To make sense of things, I ended up constructing a numerical way of thinking about melody and scales using intervals inside a modular 12-number system. I was also learning basic computer programming at the time, so the connection was fairly straightforward and useful. I treat the root as 0, and everything else as its distance (in semitones) above that, modulo 12.

This is obviously not a new idea or observation, but I don’t see it easily accessible anywhere else, so this post is just me writing down the version that ended up making the most sense to me.

The framework is simple:

- define scales as subsets of a 12-element universe,  
- pick a few tones as “stable,”  
- treat the rest as “color,”  
- and describe melodies as sequences moving between those sets.

This framework has helped me make sense, conceptually at least, of songs I like. 

---

## Universe 

Define the universe of possible notes as:

$$
U = \{0,1,2,\dots,11\} \pmod{12}
$$

where $$0$$ is the chosen root of the key.

### Frequencies 

In equal temperament, each step of this $$0-11$$ system corresponds to a constant multiplicative change in frequency. If the root has frequency $$f_0$$, the pitch class labeled $$i$$ corresponds (including octaves) to

$$
f_i = f_0 \cdot 2^{\,i/12}
$$

I don’t use this relationship for anything that follows, but it was actually this fact that motivated my use of the modular number system for notes and scales. 

---

## Scales

A scale is just a subset, often a "12 pick 7" type of problem:

$$
S \subseteq U
$$

For example, with $$0 = C$$:

- Major scale:
  $$S = \{0,2,4,5,7,9,11\}$$

- Natural minor:
  $$S = \{0,2,3,5,7,8,10\}$$

- Dorian:
  $$S = \{0,2,3,5,7,9,10\}$$

This avoids note names and focuses only on interval structure.

**Constraints:**

While mathematically any subset of $$U$$ could be a scale, most scales in practice follow these conventions:

- **Size**: Typically 5–7 notes (pentatonic through heptatonic scales)
- **Consecutive semitones**: No more than 2–3 consecutive semitone steps without a whole-step break
- **Maximum gap**: No more than 3 semitones between adjacent scale degrees
- **Contains root**: Almost always includes $$0$$ as the tonal center

These constraints ensure scales have recognizable patterns and a balance between stepwise motion and larger intervals.

---

## Stable Notes 

Inside a scale $$S$$, certain tones behave like “home base.” These are the stable tones, forming a subset:

$$
T \subseteq S
$$

In many minor or Dorian contexts, a natural choice is:

$$
T = \{0,3,7\}
$$

corresponding to the root, minor third, and fifth. In the major scale for example, these would be $$T = \{0,4,7\}$$ also 
corresponding to the root, major third, and fifth.

The color tones are just any note in the scale that is not a "stable note":

$$
C = S \setminus T
$$

These notes provide the majority of the songs complexity through motion, tension, brightness, and directional pull.

**Constraints:**

- **Size**: Typically 3 notes (a triad: root, third, fifth)
- **Must contain root**: $$0 \in T$$ for tonal stability
- **Contains the fifth**: Usually $$7 \in T$$ (the perfect fifth provides strong harmonic support)
- **Defines mode**: The third (either $$3$$ or $$4$$) typically belongs to $$T$$ and determines major vs. minor character 

---

## Melodies 

A melody can be represented as a sequence:

$$
M = \{m_1, m_2, \dots, m_n\}, \quad m_i \in S
$$

This makes it easy to talk about:

- how often the melody visits $$T$$ versus $$C$$,
- the size of intervals $$m_i \to m_{i+1}$$,
- moments of tension (moving into $$C$$ or taking larger leaps),
- and moments of resolution (landing back on $$T$$).

Small intervals and frequent returns to $$T$$ generally feel stable; longer runs inside $$C$$ feel more tense or exploratory.

**Constraints:**

Melodic movement typically follows these conventions:

- **Mostly stepwise or chord tones**: Movement is either small (1–2 semitones) or jumps between notes in the current chord $$H_i$$
- **Avoid extreme leaps**: Large jumps (> 7 semitones) are rare and usually serve dramatic purposes
- **Range**: Stay within 1–2 octaves for singable melodies
- **Cadence on stable tones**: Phrases typically end on $$t \in T$$, especially $$t = 0$$
- **Directional balance**: Extended runs in one direction are usually followed by motion in the opposite direction

---

## Chords

While melodies are sequences played over time, chords are sets of notes played simultaneously. In this framework, a chord is simply a subset:

$$
H \subseteq S
$$

Common chords are just small, specific subsets chosen for their harmonic properties:

- **Minor triad**: $$H = \{0, 3, 7\}$$
- **Major triad**: $$H = \{0, 4, 7\}$$
- **Minor 7th**: $$H = \{0, 3, 7, 10\}$$
- **Dominant 7th**: $$H = \{0, 4, 7, 10\}$$

Notice that the minor triad $$\{0, 3, 7\}$$ is exactly what we called $$T$$ in the minor/Dorian contexts earlier. This isn't a coincidence—stable tones are often chord tones. When a melody lands on $$T$$, it's landing on notes that spell out the underlying harmony.

A chord progression is then a sequence of these subsets:

$$
H_1, H_2, \dots, H_k
$$

where each $$H_i \subseteq S$$. The melody $$M$$ typically draws from the scale $$S$$, moving between the chord tones in $$H_i$$ and the remaining notes in $$S \setminus H_i$$, creating a natural interplay between the horizontal (melodic) and vertical (harmonic) dimensions.

The same notation extends naturally to more complex chords. Here are some common variations:

**Suspended chords** replace the third with a neighboring scale degree:

- **sus2**: $$H = \{0, 2, 7\}$$ — suspends the third with the major second
- **sus4**: $$H = \{0, 5, 7\}$$ — suspends the third with the perfect fourth

These chords have an open, unresolved quality because they lack the defining major or minor third.

**Sixth chords** add the sixth scale degree:

- **Major 6th**: $$H = \{0, 4, 7, 9\}$$
- **Minor 6th**: $$H = \{0, 3, 7, 9\}$$

**Extended chords** add notes beyond the seventh by borrowing from the next octave. The 9th is just the 2nd shifted up an octave ($$2 + 12 \equiv 2 \pmod{12}$$), so we represent it with the same pitch class:

- **Major 9th**: $$H = \{0, 4, 7, 11, 2\}$$ — includes major 7th and 9th (the 2)
- **Minor 9th**: $$H = \{0, 3, 7, 10, 2\}$$ — includes minor 7th and 9th
- **Dominant 9th**: $$H = \{0, 4, 7, 10, 2\}$$

Similarly, 11ths and 13ths correspond to $$5$$ and $$9$$ respectively. These extended notes often come from the underlying scale $$S$$, but played in a higher register to avoid muddiness in the lower octaves.

**Altered dominant chords** modify the 5th and/or 9th:

- **7♭5**: $$H = \{0, 4, 6, 10\}$$ — flatted fifth
- **7♯5**: $$H = \{0, 4, 8, 10\}$$ — raised fifth
- **7♭9**: $$H = \{0, 4, 7, 10, 1\}$$ — flatted ninth
- **7♯9**: $$H = \{0, 4, 7, 10, 3\}$$ — raised ninth (the "Hendrix chord")

**Diminished chords** flatten both the third and fifth:

- **Diminished triad**: $$H = \{0, 3, 6\}$$
- **Diminished 7th**: $$H = \{0, 3, 6, 9\}$$ — note the symmetry (all intervals of 3 semitones)

**Augmented chords** raise the fifth:

- **Augmented triad**: $$H = \{0, 4, 8\}$$ — also symmetric (all intervals of 4 semitones)

The interval structure makes these relationships clear. For instance, $$\{0, 5, 7\}$$ (sus4) differs from $$\{0, 4, 7\}$$ (major) by a single semitone—moving $$4 \to 5$$ creates the suspension. Similarly, the diminished 7th chord $$\{0, 3, 6, 9\}$$ divides the octave into four equal parts, which is why it sounds so symmetrical and tense.

**Constraints:**

Chords follow certain structural conventions:

- **Size**: Typically 3–5 notes (triads through 9th chords; larger chords can sound muddy)
- **Stacking thirds**: Most chords are built by stacking intervals of 3–4 semitones
- **Voice spacing**: Notes should be spread to avoid clusters (especially in lower registers)

---

## Implementation

I've implemented a version of this in Python as a music generator that creates scales, melodies, and chord progressions following the constraints described above.

**[Download music_generator.py](/assets/scripts/music_generator.py)**

Try it out:

```bash
# Generate music in C Dorian with guitar tabs
python3 music_generator.py --key C --scale dorian --tabs

# Generate a random constrained scale
python3 music_generator.py --random --tabs

# Custom melody and progression lengths
python3 music_generator.py --key A --scale pentatonic_minor \
    --melody-length 24 --progression-length 8
```

The generator outputs everything in both interval notation and note names, making it easy to see how the mathematical framework translates to actual music.

If you're in a rut with your music, give it a try! 
