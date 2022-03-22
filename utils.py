import os
from datetime import date, timedelta

curr_dir = os.path.dirname(os.path.realpath(__file__))
LOGS_DIRECTORY = os.path.join(curr_dir, 'logs/')
BATCH_DIRECTORY = os.path.join(curr_dir, 'batch/')
RESULTS_DIRECTORY = os.path.join(curr_dir, 'results/')
os.makedirs(os.path.dirname(LOGS_DIRECTORY), exist_ok=True)
os.makedirs(os.path.dirname(BATCH_DIRECTORY), exist_ok=True)
os.makedirs(os.path.dirname(RESULTS_DIRECTORY), exist_ok=True)

countries = set()
users = dict()
songs = dict()

# Calculate last 7 days, without including the current one
days = []
today = date.today()
current_day = date.today().strftime('%Y%m%d')
for i in range(1, 8):
    formatted_day = (today - timedelta(days=i)).strftime('%Y%m%d')
    days.append(formatted_day)


def get_row_info(line):
    """ Parse line information """
    cols = [x.strip() for x in line.split('|')]

    if len(cols) != 3:
        return

    sng, usr, cn = cols

    if len(cn) != 2:
        return

    return sng, usr, cn


def get_line_country(line):
    """ Parse line country """
    row = get_row_info(line)
    if row is None:
        return
    _, _, cn = row

    return cn
