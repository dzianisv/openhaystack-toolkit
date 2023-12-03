#!/usr/bin/env python3

import sys
import re
import base64
import os
import tempfile
import subprocess
import argparse

def flash(advertisement_key: str):
    advertisement_key_bin = base64.b64decode(advertisement_key)
    pattern = b"OFFLINEFINDINGPUBLICKEYHERE!"
    advertisement_key_len = len(advertisement_key_bin)
    pattern_len = len(pattern)
    if advertisement_key_len != pattern_len:
        raise ValueError(f"Invalid advertisement key lenght. Expected {pattern_len}, provided key lenght is {advertisement_key_len}")

    with open("firmware/nrf51.bin", "rb") as src_firmware, \
        tempfile.NamedTemporaryFile("wb", delete=True) as dst_firmware:
        data = src_firmware.read()
        if  pattern not in data:
            raise Exception("Invalid firmware file. Adverisement key placeholder is not found")

        patched_firmare_bin = re.sub(pattern, advertisement_key_bin, data)
        dst_firmware.write(patched_firmare_bin)

        subprocess.run([
            'openocd',
            '-f', 'interface/stlink-v2.cfg',
            '-f', 'target/nrf51.cfg',
            '-c', f'init; halt; nrf51 mass_erase; program {dst_firmware.name} verify; program {dst_firmware.name}; exit;'
        ])

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Flash the firmware')
    parser.add_argument('--advertisement-key', type=str, required=True, help='Key ID to flash')
    args = parser.parse_args()

    sys.exit(flash(args.advertisement_key))