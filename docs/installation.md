# Installing YAY Linux

YAY Linux ships a live ISO that boots directly into a working environment.
From there you use **archinstall** (Arch's official guided installer) to write
the system to disk.

---

## 1 — Download the ISO

Get the latest ISO from the
[Releases page](https://github.com/hyuuwu/yaylinux/releases) or from the
**Actions → Build YAY Linux ISO** artifact of the latest successful CI run.

---

## 2 — Write the ISO to a USB drive

Replace `/dev/sdX` with your USB device (find it with `lsblk`).

> ⚠️ This **erases** everything on the USB drive.

```bash
# Linux / macOS
sudo dd if=yaylinux-*.iso of=/dev/sdX bs=4M status=progress oflag=sync

# Windows
# Use Rufus (https://rufus.ie) — choose "DD image" mode
```

---

## 3 — Boot the live environment

1. Insert the USB drive and restart your computer.
2. Enter your firmware/BIOS boot menu (usually **F12**, **F2**, or **Del**).
3. Select the USB drive.
4. Choose **YAY Linux** from the bootloader menu.

The live system auto-logs in as `root` (no password needed).

---

## 4 — Connect to the internet

**Wi-Fi via nmtui:**
```bash
nmtui
```

**Ethernet** is automatically configured via DHCP.

Verify connectivity:
```bash
ping -c 3 archlinux.org
```

---

## 5 — Run the installer

```bash
archinstall
```

The guided installer will walk you through:
- Disk partitioning / formatting
- Region & locale
- Creating a user account & password
- Selecting a desktop environment
- Installing bootloader

When finished, type `reboot` and remove the USB drive.

---

## 6 — After installation

- **Update packages:** `sudo pacman -Syu`
- **Enable firewall:** `sudo systemctl enable --now ufw && sudo ufw enable`
- **Install the AUR helper (yay):**
  ```bash
  sudo pacman -S --needed git base-devel
  git clone https://aur.archlinux.org/yay.git
  cd yay && makepkg -si
  ```

---

## Minimum hardware requirements

| Component | Minimum        | Recommended   |
|-----------|----------------|---------------|
| CPU       | x86_64 (64-bit) | Dual-core 2 GHz+ |
| RAM       | 512 MB (live)  | 2 GB+         |
| Disk      | 8 GB           | 20 GB+        |
| Firmware  | BIOS or UEFI   | UEFI          |
