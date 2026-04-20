# Building YAY Linux from Source

This guide explains how to build the YAY Linux ISO on your own machine.

---

## Requirements

- An **Arch Linux** host system (or an Arch Linux container/VM)
- **Root / sudo** access
- `archiso` package: `sudo pacman -S archiso`
- ~4 GB of free disk space for the work tree
- Internet access (packages are downloaded from Arch mirrors)

---

## Quick build

```bash
git clone https://github.com/hyuuwu/yaylinux.git
cd yaylinux
sudo ./build.sh
```

The ISO is placed in `./out/yaylinux-*.iso`.

---

## Build options

```
sudo ./build.sh [options]

  -o <dir>   Output directory  (default: ./out)
  -c <dir>   Work directory    (default: ./work)
  -v         Verbose mkarchiso output
  -h         Show help
```

Example — build with custom directories:
```bash
sudo ./build.sh -o /tmp/yaylinux-out -c /tmp/yaylinux-work -v
```

---

## Directory layout

```
yaylinux/
├── build.sh                    Top-level build script
├── profile/                    archiso profile
│   ├── profiledef.sh           ISO identity & build modes
│   ├── packages.x86_64         Package list
│   ├── pacman.conf             Pacman configuration
│   ├── airootfs/               Files overlaid onto the live root FS
│   │   ├── etc/                System configuration
│   │   └── root/               Root home (welcome script, etc.)
│   ├── grub/grub.cfg           GRUB boot menu
│   ├── efiboot/                EFI loader entries
│   └── syslinux/               Legacy BIOS syslinux configs
├── docs/                       Documentation
│   ├── installation.md
│   └── building.md
└── .github/workflows/
    └── build-iso.yml           CI workflow (Arch container + mkarchiso)
```

---

## Customising the ISO

### Adding/removing packages

Edit `profile/packages.x86_64`. Each non-blank, non-comment line is a
package name passed to `pacman`.

### Changing the live environment

Place any files you want in the live root filesystem under
`profile/airootfs/`. The directory is merged on top of the installed
packages, so `profile/airootfs/etc/hostname` sets the live hostname.

### Changing the bootloader menu

- **GRUB (UEFI/BIOS):** edit `profile/grub/grub.cfg`
- **systemd-boot (UEFI):** edit files in `profile/efiboot/loader/`
- **syslinux (BIOS):** edit files in `profile/syslinux/`

---

## Building inside Docker / Podman

You can build the ISO without an Arch host using a container:

```bash
docker run --rm --privileged \
  -v "$(pwd):/build" \
  -w /build \
  archlinux:latest \
  bash -c "pacman -Syu --noconfirm archiso && ./build.sh -o out -c work"
```

---

## Testing the ISO

Boot the ISO in QEMU (UEFI):

```bash
# Install QEMU and OVMF
sudo pacman -S qemu-full edk2-ovmf

# Boot
qemu-system-x86_64 \
  -enable-kvm \
  -m 2G \
  -cpu host \
  -bios /usr/share/ovmf/x64/OVMF.fd \
  -cdrom out/yaylinux-*.iso \
  -boot d
```

Or with VirtualBox / VMware — simply add the ISO as a virtual optical drive.
