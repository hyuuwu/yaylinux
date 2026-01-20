import subprocess as sub
import os
import platform

def install(app):
    system_os = platform.system()
    if system_os == 'Windows':
        look4choco = sub.run(["where", "choco"], capture_output=True)
        if look4choco.returncode == 0:
            print(f"Installing {app} via Chocolatey...")
            # choco install -y requires administrative privileges usually.
            installation = sub.run(["choco", "install", app, "-y"])
            if installation.returncode == 0:
                print(f"{app} installed successfully.")
            else:
                print("Installation failed.")
        else:
            print("Chocolatey (choco) not found.")
            print("Please install Chocolatey manually or run this script as Administrator to attempt auto-installation.")
            # Auto-installing choco is risky and complex to get right in a script without explicit permission interaction.
            # Simplified for safety.
    elif system_os == 'Linux':
        distro = platform.linux_distribution()[0].lower() if hasattr(platform, 'linux_distribution') else ''
        # Modern python might not have linux_distribution, use distro package or /etc/os-release if needed. 
        # But assuming generic pacman usage as per original code context (Arch-like):
        print(f"Attempting to install {app}. You might be prompted for sudo password.")
        try:
             # Removing -S for sudo to avoid hanging if no password provided via stdin. 
             # Let it use terminal if interactive, or fail.
            sub.run(["sudo", "pacman", "-S", app])
        except Exception as e:
            print(f"Error executing installation command: {e}")
    elif system_os == 'Darwin': # macOS
        print("ts aint gon work.")
    else:
        print(f"how do you even use {system_os}")
