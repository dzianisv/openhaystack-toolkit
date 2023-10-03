#!/usr/bin/env python3

"""Script to get the icloud key from your keychain password."""

from getpass import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.ciphers.algorithms import TripleDES
from cryptography.hazmat.backends import default_backend
from openhaybike.utils import unpad, decrypt
from openhaybike.keychain import read_keychain

def get_icloud_key() -> str:
    keychain = read_keychain()
    password = getpass("Keychain password: ")
    master_key = PBKDF2HMAC(
        algorithm=hashes.SHA1(),
        length=24,
        salt=keychain.db_key_salt,
        iterations=1000,
        backend=default_backend(),
    ).derive(bytes(password, encoding="ascii"))
    db_key = unpad(
        decrypt(keychain.db_key_enc, TripleDES(master_key), CBC(keychain.db_key_IV)),
        TripleDES.block_size,
    )[:24]
    p1 = unpad(
        decrypt(
            keychain.symmetric_key_enc, TripleDES(db_key), CBC(b"J\xdd\xa2,y\xe8!\x05")
        ),
        TripleDES.block_size,
    )
    symmetric_key = unpad(
        decrypt(p1[:32][::-1], TripleDES(db_key), CBC(keychain.symmetric_key_IV)),
        TripleDES.block_size,
    )[4:]
    icloud_key = unpad(
        decrypt(
            keychain.icloud_key_enc,
            TripleDES(symmetric_key),
            CBC(keychain.icloud_key_IV),
        ),
        TripleDES.block_size,
    )
    return icloud_key


if __name__ == "__main__":
    print(get_icloud_key().decode('ascii'))

