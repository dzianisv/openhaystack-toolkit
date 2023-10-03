#!/usr/bin/env python3

from lib.AirTagCrypto import AirTagCrypto
import base64
import json
import base64
import hashlib

crypto = AirTagCrypto()

keys = {
    "key_id": base64.b64encode(hashlib.sha256(base64.b64decode(crypto.get_advertisement_key())).digest()).decode('utf-8'),
    "advertisement_key": crypto.get_advertisement_key(),
    "private_key": base64.b64encode(crypto._private_key).decode()
}

print(json.dumps(keys, indent=4))