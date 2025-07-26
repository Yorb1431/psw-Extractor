from cryptography.fernet import Fernet

with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

with open("wifi_passwords.enc", "rb") as enc_file:
    encrypted_data = enc_file.read()

decrypted_data = cipher.decrypt(encrypted_data)
print(decrypted_data.decode())
