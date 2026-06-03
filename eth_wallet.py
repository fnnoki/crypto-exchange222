import os
import struct
import hashlib
import hmac
from dotenv import load_dotenv

load_dotenv()

ETH_SEED = os.getenv('ETH_SEED', os.getenv('TRON_SEED', ''))

def mnemonic_to_seed(mnemonic, password=''):
    mnemonic = mnemonic.strip()
    salt = b'mnemonic' + password.encode('utf-8')
    seed = hashlib.pbkdf2_hmac('sha512', mnemonic.encode('utf-8'), salt, 2048)
    return seed

def derive_eth_key(seed, index=0):
    key = seed[:32]
    chain_code = seed[32:64]
    path = [44 + 0x80000000, 60 + 0x80000000, 0 + 0x80000000, 0, index]
    for idx in path:
        data = key + struct.pack('>I', idx)
        I = hmac.new(chain_code, data, hashlib.sha512).digest()
        key = I[:32]
        chain_code = I[32:64]
    return key

def private_key_to_address(private_key_hex):
    try:
        from eth_keys import keys
        pk = keys.PrivateKey(bytes.fromhex(private_key_hex))
        pub_key = pk.public_key
        addr_bytes = hashlib.sha3_256(pub_key.to_bytes()).digest()[-20:]
        address = '0x' + addr_bytes.hex()
        return address
    except ImportError:
        pass
    try:
        from coincurve import PublicKey
        pk_bytes = bytes.fromhex(private_key_hex)
        pub_key = PublicKey.from_secret(pk_bytes)
        uncompressed = pub_key.format(compressed=False)
        addr_bytes = hashlib.sha3_256(uncompressed[1:]).digest()[-20:]
        address = '0x' + addr_bytes.hex()
        return address
    except ImportError:
        pass
    return None

def create_eth_address(index=0):
    try:
        if ETH_SEED:
            seed = mnemonic_to_seed(ETH_SEED)
            key_bytes = derive_eth_key(seed, index)
            private_key_hex = key_bytes.hex()
            address = private_key_to_address(private_key_hex)
            if address:
                print(f"Generated ETH address {index}: {address}")
                return address
            print("Could not derive address, using private-key-based fallback")
            return '0x' + hashlib.sha3_256(key_bytes).digest()[-20:].hex()
        else:
            print("No ETH_SEED or TRON_SEED set")
            return None
    except Exception as e:
        print(f"Error generating ETH address: {e}")
        return None

if __name__ == "__main__":
    if ETH_SEED:
        print(f"Seed: {ETH_SEED[:20]}...")
        for i in range(3):
            addr = create_eth_address(i)
            if addr:
                print(f"Address {i}: {addr}")
    else:
        print("No seed configured. Set ETH_SEED or TRON_SEED in .env")
