import subprocess
import platform

def detect_os():
    """Detecta el sistema operativo."""
    return platform.system()

# Funciones específicas para Windows
def get_wifi_profiles_windows():
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], text=True, stderr=subprocess.DEVNULL)
        profiles = [line.split(":")[1].strip() for line in data.split("\n") if "All User Profile" in line]
        return profiles
    
    except subprocess.CalledProcessError:
        return []

def get_wifi_password_windows(profile):
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear'], text=True, stderr=subprocess.DEVNULL)
        
        for line in data.split("\n"):
            if "Key Content" in line:
                return line.split(":")[1].strip()
        return None
    
    except subprocess.CalledProcessError:
        return None

# Funciones específicas para Linux
def get_wifi_profiles_linux():
    try:
        data = subprocess.check_output(['nmcli', '-t', '-f', 'NAME', 'connection', 'show'], text=True)
        profiles = [line.strip() for line in data.split("\n") if line.strip()]
        return profiles
    
    except subprocess.CalledProcessError:
        return []

def get_wifi_password_linux(profile):
    try:
        data = subprocess.check_output(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', profile], text=True)
        return data.strip() if data.strip() else None
    
    except subprocess.CalledProcessError:
        return None

# Función principal
def main():
    os_type = detect_os()
    print(f"Detectando sistema operativo: {os_type}\n")
    print("{:<30} {:<}".format("Wi-Fi Profile", "Password"))
    print("-" * 50)
    
    if os_type == "Windows":
        profiles = get_wifi_profiles_windows()

        for profile in profiles:
            password = get_wifi_password_windows(profile)
            print("{:<30} {:<}".format(profile, password if password else "No disponible"))

    elif os_type == "Linux":
        profiles = get_wifi_profiles_linux()

        for profile in profiles:
            password = get_wifi_password_linux(profile)
            print("{:<30} {:<}".format(profile, password if password else "No disponible"))

    else:
        print("Este script solo funciona en Windows y Linux por el momento.")

if __name__ == "__main__":
    main()
