#!/usr/bin/env python3

import argparse
import json
import os
import sys
from lib.icloud import get_icloud_key
from openhaybike.types import BikeTracker
from openhaybike.locations import get_locations_of_trackers

if __name__ == "__main__":
    try:
        icloud_key = get_icloud_key()
    except ValueError as e:
        sys.stderr.write("Failed to retrieve an icloud key. Incorrect password?", str(e))
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default='trackers.json', type=str, help="Path to tracker.json file")
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
