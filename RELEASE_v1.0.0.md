# 📎 RELEASE NOTES – bitpeek.py  
**Version:** 1.0.0  
**Release Date:** 2025-05-09

---

## 🚀 Overview

**BitPeek** is a lightweight CLI tool for analyzing Bitcoin Base58 addresses.  
It focuses on decoding, structural inspection, and verifying checksums in a secure offline environment.

Designed as an educational and diagnostic utility, `bitpeek.py` helps demystify how Bitcoin addresses are encoded and validated.

---

## 🔧 Core Features

- 📦 Decodes Base58Check Bitcoin addresses (P2PKH, P2SH)  
- 🔍 Extracts version byte and payload (RIPEMD-160 hash)  
- 🧮 Verifies double SHA256 checksum  
- 📊 Displays entropy-related information: character distribution and uniqueness  
- 🖥️ Fully interactive CLI with colored output (via `colorama`)  
- 🔒 100% offline operation – no internet access required

---

## ✅ Included in v1.0.0

- ✅ `bitpeek.py` – Terminal-based tool  
- ✅ Base58 decoding with correct padding logic  
- ✅ Version byte parsing and address type mapping  
- ✅ RIPEMD-160 hash extraction from payload  
- ✅ Checksum validation using double SHA256  
- ✅ Terminal output with:
  - Full decoded hex
  - Address classification
  - Risk heuristics and symbol entropy stats
- ✅ Clear UX with input prompts and clean exit handling

---

## ⚠️ Notes

- Input must be a valid Base58Check Bitcoin address  
- Malformed addresses or invalid checksums are gracefully rejected  
- Entropy score is heuristic and for educational use only  
- Results are shown in terminal – no file output in this version

---

## 📌 Related Files

- [README.md](./README.md) – Main documentation  
- [bitpeek.py](./bitpeek.py) – CLI tool source  
- [ETHICS.md](./ETHICS.md) – Responsible usage policy  
- [RELEASE_v1.0.0.md](./RELEASE_v1.0.0.md) – This file  
- [LICENSE](./LICENSE) – Apache 2.0 license

---

## 📜 License  
Licensed under the [Apache 2.0 License](./LICENSE) by **BitMorphX**

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

🔗 GitHub: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
