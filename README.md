# BitPeek – Bitcoin Address Intelligence Toolkit

BitPeek is a forensic utility for parsing and analyzing Bitcoin addresses (Base58 format). It supports both command-line and web-based interfaces.

---

## 🔧 Features

- Bitcoin Base58 address decoding
- Version byte interpretation (mainnet/testnet, P2PKH/P2SH)
- Payload inspection with entropy analysis
- Checksum validation
- RIPEMD-160 hash display
- CLI version with colored output
- Web interface (Flask) with dark mode

---

## 🚀 Installation

1. Clone this repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

---

## 🖥️ CLI Usage

Run the terminal version:

```bash
python3 bitpeek.py
```

Features:
- Color-coded output
- Base58 decode and checksum check
- Byte distribution insight

---

## 🌐 Web Interface (Flask)

To run the web-based GUI:

```bash
python3 bitpeek_web.py
```

Then open your browser at:
```
http://localhost:5000
```

Provides:
- Dark-mode styled HTML table
- Real-time analysis
- Same logic as CLI version (Base58 decode, checksum, entropy, RIPEMD-160)

---

## 📂 File Structure

- `bitpeek.py` – CLI version
- `bitpeek_web.py` – Flask web version
- `requirements.txt` – Python dependencies
- `RELEASE_v1.0.0.md` – Release history

---

## 🧪 Requirements

```
termcolor
flask
pycryptodome
```

---

## 📜 License

MIT License — see [LICENSE](LICENSE)

---

## Disclaimer

- 🚫 This software is for **educational use only**.
- ⚠️ Do not use this tool with real cryptocurrency.
- ❗ The author takes no responsibility for losses or misuse.
- 🛡️ Use responsibly and at your own risk.

---

## 🎁 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

We also value early privacy coins such as **Bytecoin (BCN)**:  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

Created with dedication to education, blockchain exploration, and ethical research.  
*“I morph bits, not to break, but to understand.” — BitMorphX*
