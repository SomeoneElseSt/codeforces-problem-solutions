"""
Find the distribution of the strings problem.

At each step, two active strings are chosen at random. If the same string is
chosen twice, it closes and leaves the active pool (two ends are tied together). 
Otherwise, the two strings are joined and both remain active (ends still open).

Not a problem in codeforces, just didn't know where to put this code.
"""

import random
import matplotlib.pyplot as plt
from collections import Counter

NUM_TRIALS = 10000
NUM_STRINGS = 50


def run_trial(num_strings):
    # List of NUM_STRINGS ones
    active_lengths = [1 for _ in range(num_strings)]
    # Running list
    final_lengths = []

    for _ in range(num_strings):
        # If only string is left and collapsed, break
        if not active_lengths:
            break

        # Chooose two ends
        i = random.randrange(len(active_lengths))
        j = random.randrange(len(active_lengths))

        # If the ends are the same, close the string individually and remove from pool
        if i == j:
            final_lengths.append(active_lengths.pop(i))
            continue

        # If not, add together
        active_lengths[i] = active_lengths[i] + active_lengths[j]

    # Save the strings that didn't collapse by num_strings
    final_lengths.extend(active_lengths)
    return final_lengths

results = []

# Run the trial NUM_TRIALS times
for _ in range(NUM_TRIALS):
    results.extend(run_trial(NUM_STRINGS))



