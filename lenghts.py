"""
Find the distribution of the strings problem.

There are NUM_STRINGS strings, each with two ends. At each step two free ends are
picked at random and tied together. If both ends belong to the same path, that
path closes into a loop and leaves the pool. Otherwise the two paths merge into
one (still with two free ends). Count how many loops form per run.

Not a problem in codeforces, just didn't know where to put this code.
"""

import random
import matplotlib.pyplot as plt
from collections import Counter

NUM_TRIALS = 10000
NUM_STRINGS = 50


def run_trial(num_strings):
    # Two ends per path; each end stores its path's id
    ends = [k for k in range(num_strings) for _ in range(2)]
    loops = 0

    while ends:
        # Pick two free ends and tie them together
        a = ends.pop(random.randrange(len(ends)))
        b = ends.pop(random.randrange(len(ends)))

        # Both ends belong to one path: it closes into a loop
        if a == b:
            loops += 1
            continue

        # Two paths merge into one: relabel path b's leftover end as path a
        ends[ends.index(b)] = a

    return loops

results = []

# Run the trial NUM_TRIALS times
for _ in range(NUM_TRIALS):
    results.append(run_trial(NUM_STRINGS))


# Plot the distribution
loop_count_frequencies = Counter(results)
loop_counts = sorted(loop_count_frequencies.keys())
trial_frequencies = [loop_count_frequencies[count] for count in loop_counts]

plt.bar(loop_counts, trial_frequencies)
plt.xticks(loop_counts)
plt.xlabel('Number of loops')
plt.ylabel('Frequency')
plt.title(
    f'Distribution of loop counts '
    f'({NUM_TRIALS} runs, starting with {NUM_STRINGS} strings)'
)
plt.show()



