#!/usr/bin/env python

import os
import sys
from pymongo import MongoClient

from gtools.settings import load_setting


def main(fileout):

    # set the location of the settings file
    settings_file = os.path.join(os.getenv("CAPSTONE_DIR"), 'settings/project_settings.json')

    # set some settings
    database = load_setting(settings_file, 'db_name')  # name of mongodb database

    # open the connection to the database, get the table
    client = MongoClient()
    db = client[database]
    table = db['nyt-recipe-metadata']

    # get all results in the table
    results = table.find()
    with open(fileout, 'w') as f:
        for result in results:
            f.write(result['web_url'] + '\n')


if __name__ == "__main__":
    file_out = 'nyt_urls.txt'
    if len(sys.argv) > 1:
        file_out = sys.argv[0]

    cap_dir = os.getenv("CAPSTONE_DIR")
    if not os.path.isdir(os.path.join(cap_dir, 'data')):
        os.makedirs(os.path.join(cap_dir, 'data'))

    outfile = os.path.join(cap_dir, 'data', file_out)

    main(outfile)
