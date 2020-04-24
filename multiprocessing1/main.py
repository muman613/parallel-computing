"""
Example using Python multiprocessing module.
"""

import argparse
import collections
import multiprocessing
import random
import time
from modules import datasets

# Create a named tuple to contain the data
part = collections.namedtuple('part',
                              ['part',
                               'cost',
                               'quant'])


def calculate_cost(item: part) -> float:
    delay = float(random.randrange(1, 10)) / 10.0
    # print(f'Process {os.getpid()} sleeps {delay}s...')
    time.sleep(delay)
    return item.cost * item.quant


def main():
    # Parse user arguments
    parser = argparse.ArgumentParser(description='First example multiprocessing')
    parser.add_argument('--dataset', type=str, help='load data from csv file', default=None)
    options = parser.parse_args()

    parts = () # A tuple of namedtuples
    if options.dataset:
        parts = datasets.load_dataset(options.dataset)
    else:
        parts = (
            part(part='a12-56', cost=1.25, quant=1),
            part(part='a23-44', cost=1.15, quant=1),
            part(part='a23-55', cost=1.33, quant=6),
            part(part='a40-01', cost=1.07, quant=3),
            part(part='a44-22', cost=2.44, quant=2),
            part(part='a45-22', cost=4.18, quant=1),
        )

    # pprint(options)
    if parts:
        pool = multiprocessing.Pool()
        print(f'Utilizing {multiprocessing.cpu_count()} cores...')

        start_time = time.time()
        result = pool.map(calculate_cost, parts)
        end_time = time.time()
        print(f'Elapsed time = {end_time - start_time}s')

        total = 0
        for it, cost in zip(parts, result):
            total += cost

        end_time = time.time()
        print(f'Elapsed time = {end_time - start_time}s')

        print(f'Total cost {total}')


if __name__ == '__main__':
    main()
