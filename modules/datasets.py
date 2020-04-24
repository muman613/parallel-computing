import csv
import collections
import os

part = collections.namedtuple('part',
                              ['part',
                               'cost',
                               'quant'])


def load_dataset(filename:str) -> tuple:
    """
    Load data from CSV file into tuple of tuples

    :param filename: Name of CSV file to read values from
    :return: tuple of namedtuples
    """
    # print(f'load_dataset({filename})')
    parts = []
    if os.path.exists(filename):
        with open(filename, newline='') as csvfile:
            dataset_reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in dataset_reader:
                pn,pc,pq = row
                parts.append(part(part=pn,
                                  cost=pc,
                                  quant=pq))

        print(f'Loaded {len(parts)} points of data...')
    else:
        print(f'Dataset file {filename} not found.')

    return tuple(parts)
