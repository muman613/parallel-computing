"""
Example using Python multiprocessing module.
"""

import collections
import multiprocessing
import time
import os
import random
from pprint import pprint

# Create a named tuple to contain the data
part = collections.namedtuple('part',
                              ['part',
                               'cost',
                               'quant'])

# Create a tuple of part tuples
parts = (
    part('a12-56', 1.25, 1),
    part('a23-44', 1.15, 1),
    part('a23-55', 1.33, 6),
    part('a40-01', 1.07, 3),
    part('a44-22', 2.44, 2),
    part('a45-22', 4.18, 1),
)


def calculate_cost(item: part) -> float:
    delay = float(random.randrange(1, 10)) / 10.0
    print(f'Process {os.getpid()} sleeps {delay}s...')
    time.sleep(delay)
    return item.cost * item.quant


pool = multiprocessing.Pool()
print(f'Utilizing {multiprocessing.cpu_count()} cores...')

result = pool.map(calculate_cost, parts)

total = 0

for it, cost in zip(parts, result):
    total += cost

print(f'Total cost {total}')
