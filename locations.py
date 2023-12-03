#!/usr/bin/env python3

import argparse
from openhaybike.types import BikeTracker
from openhaybike.locations import get_locations_of_trackers
import json
import os
from lib.icloud import get_icloud_key

icloud_key = get_icloud_key()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="Path to tracker.json file")
    args = parser.parse_args()

    with open(args.config, 'r', encoding='utf8') as f:
        keys = json.load(f)
    
    if type(keys) is dict:
        keys = [keys]

    trackers = [ BikeTracker(
        name=tracker.get("name", tracker.get("key_id")),
        key_id=tracker.get("key_id"),
        advertisement_key=tracker.get("advertisement_key"),
        private_key=tracker.get("private_key"),
    ) for tracker in keys]

    print(get_locations_of_trackers(trackers, icloud_key, 24))
