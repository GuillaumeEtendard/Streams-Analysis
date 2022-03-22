# Streams analysis

## Solution implemented

First of all, I do a first operation on the file to get the list of countries. This will be useful later to sort by
country and make 1 file per country (and avoid opening/closing in the for loop each time we write in a country file)

Then, instead of processing the big file, I distribute it by creating batches of smaller files, by country and by day.
So for each day and each country, I will have a file containing the streams of that day that took place in that country
I also delete files older than the last 7 days to clean directory.

Once the files are written, I can compute them:
I used the counter class of the collections module of python, with a counter for the songs per country and a counter for
the songs per user I increment the counter for each record, and I delete what I don't need anymore during the
processing (the countries already processed)

At the same time, I update my new file for each country with the top 50 most listened sounds Once finished, I do the
same with the sounds by users

At the end, we get the 2 files of the day, containing the top 50 / country of the last 7 days and the top 50 / user of
the last 7 days

Here is my final architecture :

    .
    ├── batch                   # Batch files (intermediate tasks)
    ├── logs                    # Logs files (original stream files)
    ├── results                 # Results files (files computed)
    ├── batch_script.py         # Script containing functions that create batches
    ├── counter_script.py       # Script containing functions that count records and write output files
    ├── main.py                 # Main script - entry point
    ├── utils.py                # Utils functions and variables that are used in scripts
    └── README.md

## Run

To run the script every day, we have to make a cron :

```
crontab -e
```

And add this line :

```
0 6 * * * /usr/bin/python3 /path/to/main.py
```

To run it every day at 6 AM for example

I had to add ```chmod a+x /path/to/main.py``` to have permission to execute it