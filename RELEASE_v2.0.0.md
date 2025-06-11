# 📎 RELEASE NOTES – bitpeek  
**Version:** 2.0.0  
**Release Date:** 2025-06-11

---

## 🚀 Overview

This release introduces major structural, documentation, and usability improvements to BitPeek.

While the analytical core remains untouched, this version elevates the project to production-quality standards with clear documentation, interface separation, and refined naming consistency.

---

## 🆕 New in v2.0.0

- ✅ Created `bitpeek.bat` for quick Windows launch  
- ✅ Added `bitpeek_web.py`: Flask GUI version of CLI tool  
- ✅ Created `.vscode/` folder with:
  - `settings.json`
  - `launch.json`
  - `tasks.json`
  - `extensions.json`
- ✅ Added `assets/banner.png` used in README header  
- ✅ Rewritten `README.md` with:
  - Emoji sections  
  - Dual-mode usage (CLI + Flask)  
  - VSCode and structural layout  
- ✅ Added `RELEASE_v1.0.0.md` as historical changelog  
- ✅ Created `RELEASE_v2.0.0.md` (this file)  
- ✅ Clarified responsible usage in [`ETHICS.md`](./ETHICS.md)  
- ✅ Included [`NOTICE`](./NOTICE) for license attributions

---

## 🔍 Technical Notes

- Core CLI logic (`bitpeek.py`) remains unchanged  
- Flask GUI (`bitpeek_web.py`) mirrors all CLI behavior  
- CLI mode: direct prompt input  
- GUI mode: web form via `localhost:5000`

---

## 🧱 Project Structure (Post-v2.0.0)

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

## 📜 License  
Licensed under the [Apache 2.0 License](./LICENSE) by **BitMorphX**  
See [`NOTICE`](./NOTICE) for full attribution details.

---

## 🍱 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUhJPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

We also value early privacy coins such as:  
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
