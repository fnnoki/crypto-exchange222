import os
import struct
import hashlib
import hmac
import base58
import nacl.bindings as nacl
from dotenv import load_dotenv

load_dotenv()

SOLANA_SEED = os.getenv('SOLANA_SEED', os.getenv('TRON_SEED', ''))

def mnemonic_to_seed(mnemonic, password=''):
    mnemonic = mnemonic.strip()
    salt = b'mnemonic' + password.encode('utf-8')
    seed = hashlib.pbkdf2_hmac('sha512', mnemonic.encode('utf-8'), salt, 2048)
    return seed

def derive_key(seed, index=0):
    key = seed[:32]
    chain_code = seed[32:64]
    path = [44 + 0x80000000, 501 + 0x80000000, 0 + 0x80000000, 0 + 0x80000000, index]
    for idx in path:
        data = key + struct.pack('>I', idx)
        I = hmac.new(chain_code, data, hashlib.sha512).digest()
        key = I[:32]
        chain_code = I[32:64]
    return key

def create_solana_address(index=0):
    try:
        if SOLANA_SEED:
            seed = mnemonic_to_seed(SOLANA_SEED)
            key_seed = derive_key(seed, index)
            pub_key, _ = nacl.crypto_sign_seed_keypair(key_seed)
            address = base58.b58encode(pub_key).decode('ascii')
            print(f"Generated SOL address {index}: {address}")
            return address
        else:
            print("No SOLANA_SEED or TRON_SEED set")
            return None
    except Exception as e:
        print(f"Error generating SOL address: {e}")
        return None

if __name__ == "__main__":
    if SOLANA_SEED:
        print(f"Seed: {SOLANA_SEED[:20]}...")
        for i in range(3):
            addr = create_solana_address(i)
            if addr:
                print(f"Address {i}: {addr}")
    else:
        print("No seed configured. Set SOLANA_SEED or TRON_SEED in .env")
