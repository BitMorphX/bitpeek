<p align="center">
  <img src="assets/banner.png" alt="bitpeek banner" width="100%" />
</p>

# 🧬 BITPEEK V2.0.0 – BITCOIN ADDRESS ANALYZER & ENTROPY VIEWER

**bitpeek** is a CLI and Flask-powered tool for decoding and analyzing Bitcoin addresses. It verifies address format and checksum, extracts the `hash160`, and evaluates entropy distribution.

- ✅ Decodes Base58Check (P2PKH, P2SH) addresses  
- ✅ Verifies format, version prefix, and checksum  
- ✅ Extracts and displays RIPEMD-160 (hash160)  
- ✅ Calculates entropy (symbol frequency analysis)  
- ✅ Includes Flask GUI for interactive use  

---

## ⚙️ Features

- 🔍 Address decoding with Base58Check and RIPEMD-160 output  
- 🧮 Checksum verification using double SHA256  
- 📊 Entropy visualization from symbol distribution  
- 🧵 CLI & Flask GUI dual-mode usage  
- 📁 Offline-only – no remote API or data usage  

---

## 📁 File Overview

- `bitpeek.py` – CLI analysis tool  
- `bitpeek_web.py` – Flask-based GUI interface  
- `bitpeek.bat` – Quick launcher for Windows  
- `.vscode/` – VSCode configs  
- `requirements.txt` – Python dependencies  
- `LICENSE`, `NOTICE` – Licensing and attribution  
- `README.md` – This documentation  
- `ETHICS.md` – Ethical usage policy  
- `RELEASE_v1.0.0.md` – Initial release notes  
- `RELEASE_v2.0.0.md` – Refactored structure & documentation

---

## 🛠️ Dependencies

```bash
flask
base58
colorama
tqdm
```

Install with:

```bash
pip install -r requirements.txt
```

> Python 3.7+ is recommended.

---

## 📄 Release Info

Current version: **v2.0.0**  
📄 See full notes in [`RELEASE_v2.0.0.md`](./RELEASE_v2.0.0.md)

---

## 🚀 Usage

### 💻 CLI Mode

Run:

```bash
python bitpeek.py
```

You’ll be prompted to enter a Bitcoin Base58 address.  
It will:

- Decode and verify address checksum  
- Display version byte, address type, and hash160  
- Analyze entropy from the payload  
- Show symbolic uniqueness and risk assessment  

---

### 🌐 Flask GUI Mode

Run:

```bash
python bitpeek_web.py
```

Then open:

```
http://127.0.0.1:5000
```

You’ll be able to input addresses via browser form and see results.

---

## 📂 Project Structure

```text
bitpeek/
├── assets/
│   └── banner.png
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   ├── tasks.json
│   └── extensions.json
├── bitpeek.py
├── bitpeek_web.py
├── bitpeek.bat
├── LICENSE
├── NOTICE
├── ETHICS.md
├── README.md
├── RELEASE_v1.0.0.md
├── RELEASE_v2.0.0.md
└── requirements.txt
```

---

## ⚠️ DISCLAIMER

This software is provided strictly for **educational, analytical, and research purposes only**.  
The author **does not condone unethical behavior**, unauthorized access, or blockchain abuse.

**Use responsibly. Learn ethically. Contribute honestly.**

---

## ⚖️ Ethical Use

See [`ETHICS.md`](./ETHICS.md)

> ❗ Do not use this tool to attempt key collisions or unauthorized activity.  
> 🧠 Use responsibly and with integrity.

---

## 📜 License

Licensed under the [Apache 2.0 License](./LICENSE) by **BitMorphX**

---

## 📣 NOTICE

See [`NOTICE`](./NOTICE) for attribution, license requirements, and third-party credits.

---

## 🍱 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUhJPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

**We also value early privacy coins such as:**  
★ **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

## 👤 Author & Contact

🔗 GitHub Profile: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
