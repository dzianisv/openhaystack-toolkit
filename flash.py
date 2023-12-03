#!/usr/bin/env python3

import sys
import re
import base64
import os
import tempfile
import subprocess
import argparse

def flash(advertisement_key: str):
    with open("firmware/nrf51822.bin", "rb") as src_firmware, \
        tempfile.NamedTemporaryFile("wb", delete=True) as dst_firmware:

        decoded_bytes = base64.b64decode(advertisement_key)
        data = src_firmware.read()
        output_string = re.sub(b"OFFLINEFINDINGPUBLICKEYHERE!", decoded_bytes, data)
        dst_firmware.write(output_string)

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