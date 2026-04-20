# YAY Linux

> **A fun, rolling-release Linux distribution based on Arch Linux.**

[![Build YAY Linux ISO](https://github.com/hyuuwu/yaylinux/actions/workflows/build-iso.yml/badge.svg)](https://github.com/hyuuwu/yaylinux/actions/workflows/build-iso.yml)

---

## What is YAY Linux?

YAY Linux is an Arch-based live/install ISO aimed at being approachable,
fast, and fun. It ships with:

- **Arch Linux base** — rolling release, up-to-date packages
- **XFCE desktop** — lightweight and snappy
- **archinstall** — guided installer, no manual partitioning required
- **NetworkManager** — easy wired & Wi-Fi setup out of the box
- **GRUB + systemd-boot** — UEFI and legacy BIOS support

---

## Download

Grab the latest ISO from the
[**Releases page**](https://github.com/hyuuwu/yaylinux/releases), or from
the latest successful
[**CI build artifact**](https://github.com/hyuuwu/yaylinux/actions/workflows/build-iso.yml).

---

## Quick start

1. [Download the ISO](https://github.com/hyuuwu/yaylinux/releases)
2. Flash it to a USB drive (`dd` / Rufus)
3. Boot from USB
4. Run `archinstall` in the live terminal
5. Reboot into your new system 🎉

See **[docs/installation.md](docs/installation.md)** for the full guide.

---

## Build it yourself

```bash
# Requires an Arch Linux host with archiso installed
sudo pacman -S archiso
git clone https://github.com/hyuuwu/yaylinux.git
cd yaylinux
sudo ./build.sh
```

ISO lands in `./out/`. See **[docs/building.md](docs/building.md)** for details
and Docker / QEMU instructions.

---

## Minimum hardware

| CPU | RAM | Disk | Firmware |
|-----|-----|------|----------|
| x86_64 (64-bit) | 512 MB | 8 GB | BIOS or UEFI |

---

## Contributing

Issues and pull requests are welcome! Check the
[issue tracker](https://github.com/hyuuwu/yaylinux/issues) for ideas.
