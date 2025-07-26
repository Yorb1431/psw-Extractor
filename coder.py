import subprocess
from cryptography.fernet import Fernet

with open("key.key", "wb") as key_file:
    key = Fernet.generate_key()
    key_file.write(key)

with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

profiles_output = subprocess.check_output(
    "netsh wlan show profiles", shell=True, text=True
)
lines = profiles_output.splitlines()

wifi_names = [
    line.split(":")[1].strip()
    for line in lines if "All User Profile" in line
]

output_data = ""
for name in wifi_names:
    try:
        wifi_info = subprocess.check_output(
            f'netsh wlan show profile name="{name}" key=clear',
            shell=True,
            text=True
        )
        password_line = [line for line in wifi_info.split(
            '\n') if "Key Content" in line]
        if password_line:
            password = password_line[0].split(":")[1].strip()
            output_data += f"SSID: {name}, Password: {password}\n"
        else:
            output_data += f"SSID: {name}, Password: Not found\n"
    except subprocess.CalledProcessError as e:
        output_data += f"Error retrieving info for {name}: {e}\n"

encrypted_data = cipher.encrypt(output_data.encode())

with open("wifi_passwords.enc", "wb") as enc_file:
    enc_file.write(encrypted_data)
