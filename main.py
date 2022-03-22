#!/usr/bin/python

import time

from batch_script import create_batch_files, get_all_countries, clean_old_batch_files
from counter_script import process_batch_files


def main():
    print(f'Start process')
    get_all_countries()
    clean_old_batch_files()
    create_batch_files()
    process_batch_files()
    print(f'End process')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Execution duration : {end - start}s')
