from flask import Flask, render_template_string, request
import hashlib

app = Flask(__name__)

alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
base58_map = {char: index for index, char in enumerate(alphabet)}

def base58_decode(s):
    num = 0
    for char in s:
        num *= 58
        num += base58_map.get(char, 0)
    combined = num.to_bytes((num.bit_length() + 7) // 8, 'big')
    n_pad = len(s) - len(s.lstrip('1'))
    return b'\x00' * n_pad + combined

def get_address_type(version_hex):
    types = {
        "00": "P2PKH (mainnet)",
        "05": "P2SH (mainnet)",
        "6f": "P2PKH (testnet)",
        "c4": "P2SH (testnet)"
    }
    return types.get(version_hex.lower(), "Unknown")

def enrich_analysis(version, payload):
    version_info = {
        "00": "Standard Bitcoin mainnet address (P2PKH).",
        "05": "Pay-to-Script-Hash mainnet (P2SH).",
        "6f": "Testnet address (P2PKH).",
        "c4": "Testnet P2SH address."
    }
    unique_chars = len(set(payload))
    risk = "Low" if version not in ("6f", "c4") else "Testnet only"
    if unique_chars < 5:
        risk = "⚠ Low entropy – risky"

    ripemd160_hash = payload  # payload jau yra RIPEMD160 hash (20 baitų public key hash)

    return version_info.get(version, "Unknown type"), len(payload) // 2, unique_chars, risk, ripemd160_hash

def analyze_address(address):
    try:
        decoded = base58_decode(address)
        version = decoded[0:1].hex()
        payload = decoded[1:-4].hex()
        checksum = decoded[-4:].hex()
        calc_checksum = hashlib.sha256(hashlib.sha256(decoded[:-4]).digest()).digest()[:4].hex()

        if checksum != calc_checksum:
            return {"error": f"❌ Invalid checksum. Expected {calc_checksum}, got {checksum}"}

        addr_type = get_address_type(version)
        info, length, unique, risk, ripemd = enrich_analysis(version, payload)

        return {
            "status": "✔ Address is valid",
            "type": addr_type,
            "version": version,
            "length": f"{length} bytes",
            "unique": unique,
            "risk": risk,
            "info": info,
            "ripemd160": ripemd
        }

    except Exception as e:
        return {"error": f"⚠ Error: {e}"}

HTML_TEMPLATE = """
<!doctype html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>BitPeek Web</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #0d1f2d;
      color: #ffffff;
      padding: 2rem;
    }
    h2 {
      color: #ffffff;
    }
    form {
      margin-bottom: 1rem;
    }
    input[type=text] {
      width: 60%; padding: 0.5rem; font-size: 1rem;
      border: 1px solid #ccc; border-radius: 4px;
    }
    input[type=submit] {
      padding: 0.5rem 1rem; font-size: 1rem;
      background-color: #1e90ff; color: white;
      border: none; border-radius: 4px;
      cursor: pointer;
    }
    input[type=submit]:hover {
      background-color: #0066cc;
    }
    table {
      border-collapse: collapse; margin-top: 1rem;
      background-color: #1b2a38; color: #ffffff;
    }
    th, td {
      text-align: left; padding: 8px 12px;
      border: 1px solid #555;
    }
    th {
      background-color: #243b53;
      font-weight: bold;
    }
    .error {
      color: #ff4c4c; font-weight: bold;
    }
  </style>
</head>
<body>
<h2>BitPeek – Bitcoin Address Analyzer</h2>
<form method=post>
  <input type=text name=address placeholder="Enter Base58 Bitcoin Address">
  <input type=submit value=Analyze>
</form>

{% if result.error %}
  <p class="error">{{ result.error }}</p>
{% elif result.status %}
  <table>
    <tr><th>Status</th><td>{{ result.status }}</td></tr>
    <tr><th>Type</th><td>{{ result.type }}</td></tr>
    <tr><th>Version byte</th><td>{{ result.version }}</td></tr>
    <tr><th>Payload length</th><td>{{ result.length }}</td></tr>
    <tr><th>Unique characters</th><td>{{ result.unique }}</td></tr>
    <tr><th>Risk level</th><td>{{ result.risk }}</td></tr>
    <tr><th>Info</th><td>{{ result.info }}</td></tr>
    <tr><th>RIPEMD-160 hash</th><td>{{ result.ripemd160 }}</td></tr>
  </table>
{% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        address = request.form['address']
        result = analyze_address(address)
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
