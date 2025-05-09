#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import platform
import os

# Base58 setup
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
base58_map = {char: index for index, char in enumerate(alphabet)}

def base58_decode(s):
    num = 0
    for char in s:
        num *= 58
        num += base58_map[char]
    combined = num.to_bytes((num.bit_length() + 7) // 8, 'big')
    n_pad = len(s) - len(s.lstrip('1'))
    return b'\x00' * n_pad + combined

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def print_colored(text, color="white"):
    print(text)

def get_address_type(version_hex: str) -> str:
    version_map = {
        "00": "P2PKH (mainnet)",
        "05": "P2SH (mainnet)",
        "6f": "P2PKH (testnet)",
        "c4": "P2SH (testnet)"
    }
    return version_map.get(version_hex.lower(), "Unknown or non-standard")

def enrich_base58_analysis(version, payload):
    version_expl = {
        "00": "Standard Bitcoin mainnet address (P2PKH). Used for typical personal wallets.",
        "05": "Pay-to-Script-Hash mainnet (P2SH). Often used in multisig wallets.",
        "6f": "Testnet address (P2PKH). For development and testing purposes.",
        "c4": "Testnet P2SH address. Used in testnet multisig wallets."
    }
    risk_level = "Low"
    if version in ("6f", "c4"):
        risk_level = "Testnet (Not for real transactions)"
    elif len(set(payload)) < 5:
        risk_level = "⚠ Low entropy – possibly malformed"

    hex_length = len(payload) // 2
    return {
        "version_info": version_expl.get(version, "Unknown or custom address version."),
        "hash_length": hex_length,
        "unique_chars": len(set(payload)),
        "risk": risk_level
    }

def decode_base58_address(address: str):
    try:
        decoded = base58_decode(address)
        hex_full = decoded.hex()
        version = decoded[0:1].hex()
        payload = decoded[1:-4].hex()
        checksum = decoded[-4:].hex()

        calculated_checksum = hashlib.sha256(
            hashlib.sha256(decoded[:-4]).digest()
        ).digest()[:4].hex()

        print_colored("\nBase58 decoded (hex):      " + hex_full, "white")
        print_colored(f"Version byte:              {version}", "yellow")
        print_colored(f"Address type:              {get_address_type(version)}", "white")
        print_colored(f"Payload (RIPEMD-160):      {payload}", "white")
        print_colored(f"Checksum (from address):   {checksum}", "cyan")
        print_colored(f"Recalculated checksum:     {calculated_checksum}", "cyan")

        if checksum == calculated_checksum:
            print_colored("\n✔ Checksum is VALID", "green")
        else:
            print_colored("\n✘ Checksum is INVALID", "red")
            return

        extra = enrich_base58_analysis(version, payload)
        print_colored("\n📊 Additional analysis:", "magenta")
        print_colored(f"- Type Info:               {extra['version_info']}", "white")
        print_colored(f"- Payload Hash Length:     {extra['hash_length']} bytes", "white")
        print_colored(f"- Unique Payload Characters: {extra['unique_chars']}", "white")
        print_colored(f"- Risk Level:              {extra['risk']}", "red" if "⚠" in extra['risk'] else "green")

    except Exception as e:
        print_colored(f"Error: {e}", "red")

def main():
    clear_screen()
    print_colored("🔍 BitPeek: Bitcoin Address Inspector", "cyan")
    print_colored("─────────────────────────────────────", "cyan")
    address = input("Enter Bitcoin address (Base58): ").strip()
    decode_base58_address(address)

if __name__ == "__main__":
    main()
