# 📦 CHANGELOG – BitPeek

All notable changes to this project will be documented in this file.

---

## [v2.0.0] – 2025-06-11
📄 See full: [RELEASE_v2.0.0.md](./RELEASE_v2.0.0.md)

### 🎯 Highlights

- ✅ Created `bitpeek.bat` for quick Windows launch
- ✅ Added `bitpeek_web.py`: Flask GUI version of CLI tool
- ✅ Added `assets/banner.png` for use in README header
- ✅ Rewritten `README.md` with:
  - Emoji sections
  - Dual-mode usage (CLI + Flask)
  - VSCode and structural layout
- ✅ Introduced `.vscode/` folder with:
  - `settings.json`
  - `launch.json`
  - `tasks.json`
  - `extensions.json`
- ✅ Added full project structure display in docs
- ✅ Created `RELEASE_v1.0.0.md` and `RELEASE_v2.0.0.md`
- ✅ Updated [`NOTICE`](./NOTICE) and [`ETHICS.md`](./ETHICS.md)
- ✅ Switched LICENSE to Apache 2.0

---

## [v1.1.0] – 2025-05-25
📄 Partial entry – no standalone release notes

### ➕ Added

- Flask-based web interface (`bitpeek_web.py`)
- HTML output table layout with dark mode
- Real-time decoding of Base58 addresses
- RIPEMD-160 hash extraction and checksum validation
- Fully mirrors CLI logic in structured web UI

---

## [v1.0.0] – 2025-05-09
📄 See full: [RELEASE_v1.0.0.md](./RELEASE_v1.0.0.md)

### 🚀 Initial Release – BitPeek

First public release of **BitPeek** – a Bitcoin Base58 address inspection tool.

#### ✨ Features

- Decode any Bitcoin Base58Check address
- Identify address type (P2PKH, P2SH, testnet)
- Validate checksum (correct or invalid)
- Show version byte, payload hash, and checksum in HEX
- Provide extended analysis:
  - Address type description
  - Payload entropy and uniqueness
  - Risk level estimation
- Clean and colorful terminal output (via `colorama`)
- No internet connection required
- Runs on Windows, Linux, macOS (cross-platform)

---

### 🔧 Installation

```bash
pip install -r requirements.txt
```

---

### 🚀 Usage

```bash
python bitpeek.py
```

Then enter a Base58 Bitcoin address when prompted.

---

📚 Created with a focus on educational use, transparency, and simplicity.
