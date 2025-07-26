# 🔐 Wi-Fi Password Extractor (Encrypted Storage Edition)

This project is a **secure and encrypted Wi-Fi password extractor** built for Windows systems. It uses the Windows command-line tool `netsh` to gather stored Wi-Fi profiles and their corresponding passwords, then encrypts the results using the strong symmetric encryption algorithm **Fernet (AES-128 under the hood)**.

---

## 📁 Project Files

| File              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `coder.py`        | Main script to extract Wi-Fi credentials and encrypt the output             |
| `decoder.py`      | Decrypts and prints the encrypted credentials                               |
| `key.key`         | Encryption key used for both encoding and decoding (keep this private!)     |
| `wifi_passwords.enc` | Encrypted output of all stored Wi-Fi SSIDs and their passwords           |
| `run.bat`         | Batch script to run `coder.py` easily from Windows                          |
| `.env`            | Placeholder for optional configuration or future expansion                  |
| `README.md`       | Complete documentation for the project                                      |

---

## 🚀 Getting Started

### ✅ Requirements

- 🐍 Python 3.7 or higher
- 🪟 Windows system (uses `netsh` command)
- 📦 Python dependency:
  ```bash
  pip install cryptography
  ```

---

## ▶️ Usage Instructions

### 📦 1. Extract and Encrypt Wi-Fi Passwords

Run the extractor either via:

```bash
python coder.py
```

Or by double-clicking `run.bat`.

This will:
- Collect all saved Wi-Fi SSIDs and their passwords
- Encrypt the result using a newly generated key
- Save it to `wifi_passwords.enc`

📝 **Note:** The script generates a `key.key` file automatically on first run. Keep it safe!

---

### 🔓 2. Decrypt the Wi-Fi Passwords

To decrypt and display the encrypted Wi-Fi credentials:

```bash
python decoder.py
```

This will:
- Load `key.key`
- Decrypt `wifi_passwords.enc`
- Display results in the terminal

---

## 📌 Example Output (After Decryption)

```
SSID: MyHomeWiFi, Password: mypassword123
SSID: OfficeNet, Password: securepass456
SSID: MobileHotspot, Password: 09876wifi
```

---

## 🔒 Security Recommendations

- 🔑 **NEVER share `key.key`**. It can be used to decrypt your sensitive Wi-Fi credentials.
- 🧳 Store `key.key` on a USB stick if you're transferring encrypted files to another system.
- 🧼 Delete `wifi_passwords.enc` and `key.key` if you're done using them.
- 🔐 For enhanced security, consider modifying the script to:
  - Use a passphrase instead of saving `key.key` to disk
  - Encrypt with user-defined passwords via `PBKDF2HMAC`

---


## 🧽 Cleanup Instructions

To wipe all sensitive data:

```bash
del wifi_passwords.enc
del key.key
```

Or manually delete:
- `wifi_passwords.enc`
- `key.key`

---

## ❓ Troubleshooting

- **Empty or missing passwords**: Some profiles may not store a password, or admin rights may be required.
- **Invalid token**: Ensure the same `key.key` file is used to decrypt as was used to encrypt.
- **Permission denied**: Run the script or batch file as Administrator.
- **Command not found**: This script is designed for Windows. It will not run on Linux or macOS.

---

## 📬 Final Notes

This project was created for personal use, learning, and secure password handling. Customize it further to suit your needs or integrate it into larger systems responsibly.

---
