# 🔐 Wi-Fi Password Extractor (Encrypted Output)

This script extracts saved Wi-Fi SSIDs and their passwords from a Windows system and stores them in an encrypted file.

## 📦 Files Included

- `coder.py` → Extracts and encrypts Wi-Fi passwords into `wifi_passwords.enc`
- `decoder.py` → Decrypts and prints the encrypted output
- `key.key` → Symmetric encryption key (⚠️ Keep this file safe!)
- `run.bat` → Simple batch file to run the extractor
- `.env` → Placeholder for optional environment configuration
- `README.md` → This file

## 🛠️ Setup

1. Install dependencies:
   ```bash
   pip install cryptography
   ```

2. Run the batch script or directly use:
   ```bash
   python coder.py
   ```

3. To decrypt and view passwords:
   ```bash
   python decoder.py
   ```

## ⚠️ Security Warning

- Anyone with access to `key.key` can decrypt the passwords.
- For better security, store `key.key` on a separate device or USB stick.

## ✅ Example Output (after decryption)

```
SSID: MyWiFiHome, Password: mysecret123
SSID: CafeWiFi, Password: coffeetime456
```

## 💬 Author

Generated securely with ❤️ by ChatGPT for Yorbe.
