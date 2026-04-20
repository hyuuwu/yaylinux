#!/usr/bin/env bash
# build.sh — Build the YAY Linux ISO using archiso
#
# Usage:
#   sudo ./build.sh              Build to ./out/
#   sudo ./build.sh -o /tmp/out  Custom output directory
#   sudo ./build.sh -c /tmp/work Custom work directory
#   sudo ./build.sh -v           Verbose mode
#   sudo ./build.sh -h           Show help

set -euo pipefail

PROFILE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/profile" && pwd)"
OUT_DIR="$(pwd)/out"
WORK_DIR="$(pwd)/work"
VERBOSE=""

usage() {
    cat <<EOF
Usage: sudo $0 [options]

Options:
  -o <dir>   Output directory for the ISO (default: ./out)
  -c <dir>   Work/scratch directory       (default: ./work)
  -v         Verbose mkarchiso output
  -h         Show this help message

Requirements:
  - Arch Linux host (or Arch container)
  - archiso package installed (pacman -S archiso)
  - Run as root (sudo)
EOF
}

while getopts "o:c:vh" opt; do
    case "$opt" in
        o) OUT_DIR="$OPTARG" ;;
        c) WORK_DIR="$OPTARG" ;;
        v) VERBOSE="-v" ;;
        h) usage; exit 0 ;;
        *) usage; exit 1 ;;
    esac
done

# ── Sanity checks ──────────────────────────────────────────────────────────────
if [[ $EUID -ne 0 ]]; then
    echo "[error] This script must be run as root (use sudo)." >&2
    exit 1
fi

if ! command -v mkarchiso &>/dev/null; then
    echo "[error] mkarchiso not found. Install it with: pacman -S archiso" >&2
    exit 1
fi

# ── Build ──────────────────────────────────────────────────────────────────────
mkdir -p "$OUT_DIR" "$WORK_DIR"

echo "[yaylinux] Building ISO from profile: ${PROFILE_DIR}"
echo "[yaylinux] Output directory:          ${OUT_DIR}"
echo "[yaylinux] Work directory:            ${WORK_DIR}"
echo ""

# shellcheck disable=SC2086
mkarchiso ${VERBOSE} \
    -w "$WORK_DIR" \
    -o "$OUT_DIR" \
    "$PROFILE_DIR"

echo ""
echo "[yaylinux] Build complete!"
ls -lh "${OUT_DIR}"/*.iso 2>/dev/null || true
