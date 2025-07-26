import subprocess

profiles_output = subprocess.check_output(
    "netsh wlan show profiles", shell=True, text=True
)

lines = profiles_output.splitlines()

wifi_names = [
    line.split(":")[1].strip()
    for line in lines if "All User Profile" in line
]

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
            print(f"SSID: {name}, Password: {password}")
        else:
            print(f"SSID: {name}, Password: Not found")
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving info for {name}: {e}")

with open("wifi_passwords.txt", "w") as file:
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
                file.write(f"SSID: {name}, Password: {password}\n")
            else:
                file.write(f"SSID: {name}, Password: Not found\n")
        except subprocess.CalledProcessError as e:
            file.write(f"Error retrieving info for {name}: {e}\n")
