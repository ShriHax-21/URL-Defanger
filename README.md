# URL Defanger

This Python script provides a simple and safe method to **defang URLs** for use in cybersecurity contexts. Defanging a URL prevents accidental clicks or automatic execution by email clients, browsers, or analysis tools, making it safe to share malicious URLs in reports, logs, or threat intelligence communications.

---

## 🔧 Features

- Converts `http` and `https` to `hxxp` and `hxxps`
- Replaces `.` with `[.]` to neutralize domain names and IP addresses
- Lightweight and easy to integrate into other tools or scripts

---


# Run the Script

`python defang.py`
