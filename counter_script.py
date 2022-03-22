from collections import Counter
from utils import *


def process_batch_files():
    """ Process batch files to count records and save them """
    print('Processing batch files ...')

    for cn in countries:
        for day in days:
            with open(f'{BATCH_DIRECTORY}listen-{cn}-{day}.log') as file:
                for line in file:
                    count_record(line)
        save_top_country_songs(cn)
        songs[cn].clear()
    print(f'Top 50 songs by country wrote for day {current_day}')

    save_top_users_songs()
    print(f'Top 50 users songs wrote for {current_day}')

    print('Batch files processes ended')


def count_record(line):
    """ Increment records with the line """
    row = get_row_info(line)
    if row is None:
        return
    sng, usr, cn = row

    if usr not in users:
        users[usr] = Counter()

    if cn not in songs:
        songs[cn] = Counter()

    users[usr][sng] += 1
    songs[cn][sng] += 1


def save_top_country_songs(country):
    """ Get and save top country songs file """
    most_listened_songs = songs[country].most_common(50)

    country_top = f'{country}|'
    country_top += ','.join([f'{val[0]}:{val[1]}' for val in most_listened_songs])

    with open(f'{RESULTS_DIRECTORY}country_top50_{current_day}.txt', 'a') as f:
        f.write(f'{country_top}\n')


def save_top_users_songs():
    """ Get and save top songs for users file """
    with open(f'{RESULTS_DIRECTORY}users_top50_{current_day}.txt', 'a') as f:
        for usr in users:
            most_listened_songs = users[usr].most_common(50)

            user_top = f'{usr}|'
            user_top += ','.join([f'{val[0]}:{val[1]}' for val in most_listened_songs])

            f.write(f'{user_top}\n')
