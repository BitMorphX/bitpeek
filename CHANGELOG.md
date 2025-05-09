# 🚀 Release v1.0.0 – BitPeek

First public release of **BitPeek** – a Bitcoin Base58 address inspection tool.

## ✨ Features

- Decode any Bitcoin Base58Check address
- Identify address type (P2PKH, P2SH, testnet)
- Validate checksum (correct or invalid)
- Show version byte, payload hash, and checksum in HEX
- Provide extended analysis:
  - Address type description
  - Payload entropy and uniqueness
  - Risk level estimation
- Clean and colorful terminal output (termcolor)
- No internet connection required
- Runs on Windows, Linux, macOS (cross-platform)

---

## 🔧 Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python bitpeek.py
```

Then enter a Base58 Bitcoin address when prompted.

---

Created with a focus on educational use, transparency, and simplicity.
