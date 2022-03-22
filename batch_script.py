from os import path
from utils import *
import glob


def get_all_countries():
    """ Add all countries in files to countries set """
    print('Fetching all countries ...')
    for day in days:
        file_day_path = f'{LOGS_DIRECTORY}listen-{day}.log'
        if path.exists(file_day_path):
            with open(file_day_path, 'r') as file:
                countries.update({get_line_country(line) for line in file})
                countries.remove(None)

    print(f'Countries fetched', countries)


def clean_old_batch_files():
    """ Clean file that are not in the last 7 days to clean batch directory"""
    files = [glob.glob(f'{BATCH_DIRECTORY}*-{day}.log') for day in days]
    flattened = [file for sublist in files for file in sublist]

    for filename in os.listdir(BATCH_DIRECTORY):
        filename = f'{BATCH_DIRECTORY}{filename}'
        if filename not in flattened:
            os.remove(filename)
            print('Remove old file', filename)


def create_batch_files():
    """ Create batch files for each days and countries """
    print('Creating batch files ...')

    for day in days:
        for country in countries:
            batch_file_path = f'{BATCH_DIRECTORY}listen-{country}-{day}.log'

            # no need to recreate batch files for previous days
            if path.exists(batch_file_path):
                continue

            write_country_file(country, day, batch_file_path)

    print('Batch files created')


def write_country_file(country, day, batch_file_path):
    """ Write batch file for country and day """
    with open(batch_file_path, 'w') as batch_file:
        file_day_path = f'{LOGS_DIRECTORY}listen-{day}.log'
        with open(file_day_path, 'r') as file:
            for line in file:
                write_line_country_file(line, batch_file, country)


def write_line_country_file(line, batch_file, country):
    """ Write line in batch file """
    row = get_row_info(line)
    if row is None:
        return
    sng, usr, cn = row

    if cn != country:
        return

    batch_file.write(line)
