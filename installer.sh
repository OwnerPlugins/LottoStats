#!/bin/bash
## setup command=wget -q --no-check-certificate https://raw.githubusercontent.com/OwnerPlugins/LottoStats/main/installer.sh -O - | /bin/bash

version='1.0'
changelog='\nInitial release\nLotto statistics plugin for Enigma2'

TMPPATH=/tmp/LottoStatistiche-install
FILEPATH=/tmp/LottoStatistiche-main.tar.gz

echo "Starting LottoStatistiche installation..."

if [ ! -d /usr/lib64 ]; then
    PLUGINPATH=/usr/lib/enigma2/python/Plugins/Extensions/LottoStatistiche
else
    PLUGINPATH=/usr/lib64/enigma2/python/Plugins/Extensions/LottoStatistiche
fi

cleanup() {
    echo "Cleaning up temporary files..."
    [ -d "$TMPPATH" ] && rm -rf "$TMPPATH"
    [ -f "$FILEPATH" ] && rm -f "$FILEPATH"
    [ -d "/tmp/LottoStatistiche-main" ] && rm -rf "/tmp/LottoStatistiche-main"
}

detect_os() {
    if [ -f /var/lib/dpkg/status ]; then
        OSTYPE="DreamOs"
        STATUS="/var/lib/dpkg/status"
    elif [ -f /etc/opkg/opkg.conf ] || [ -f /var/lib/opkg/status ]; then
        OSTYPE="OE"
        STATUS="/var/lib/opkg/status"
    else
        OSTYPE="Unknown"
        STATUS=""
    fi
    echo "Detected OS type: $OSTYPE"
}

detect_os

cleanup
mkdir -p "$TMPPATH"

if ! command -v wget >/dev/null 2>&1; then
    echo "Installing wget..."
    case "$OSTYPE" in
        "DreamOs")
            apt-get update && apt-get install -y wget || { echo "Failed to install wget"; exit 1; }
            ;;
        "OE")
            opkg update && opkg install wget || { echo "Failed to install wget"; exit 1; }
            ;;
        *)
            echo "Unsupported OS type. Cannot install wget."
            exit 1
            ;;
    esac
fi

# ============================================================
# NO EXTRA DEPENDENCIES NEEDED - Only standard Enigma2 libs
# ============================================================

echo "Downloading LottoStatistiche..."
wget --no-check-certificate 'https://github.com/OwnerPlugins/LottoStats/archive/refs/heads/main.tar.gz' -O "$FILEPATH"
if [ $? -ne 0 ]; then
    echo "Failed to download LottoStatistiche package!"
    cleanup
    exit 1
fi

echo "Extracting package..."
tar -xzf "$FILEPATH" -C "$TMPPATH"
if [ $? -ne 0 ]; then
    echo "Failed to extract LottoStatistiche package!"
    cleanup
    exit 1
fi

# ============================================================
# INSTALL PLUGIN FILES
# ============================================================
echo "Installing plugin files..."
mkdir -p "$PLUGINPATH"

# Cerca la cartella LottoStatistiche
SOURCE_DIR=$(find "$TMPPATH" -type d -iname "LottoStatistiche" 2>/dev/null | head -1)

if [ -n "$SOURCE_DIR" ]; then
    echo "Found plugin directory: $SOURCE_DIR"
    cp -r "$SOURCE_DIR"/* "$PLUGINPATH/" 2>/dev/null
    echo "Copied from $SOURCE_DIR"
else
    # Fallback: cerca la struttura standard
    FOUND=0
    for dir in "$TMPPATH"/*/usr/lib/enigma2/python/Plugins/Extensions/LottoStatistiche; do
        if [ -d "$dir" ]; then
            cp -r "$dir"/* "$PLUGINPATH/" 2>/dev/null
            echo "Copied from $dir"
            FOUND=1
            break
        fi
    done
    if [ $FOUND -eq 0 ]; then
        for dir in "$TMPPATH"/*/usr/lib64/enigma2/python/Plugins/Extensions/LottoStatistiche; do
            if [ -d "$dir" ]; then
                cp -r "$dir"/* "$PLUGINPATH/" 2>/dev/null
                echo "Copied from $dir"
                FOUND=1
                break
            fi
        done
    fi
    if [ $FOUND -eq 0 ]; then
        echo "Could not find plugin files in extracted archive"
        echo "Available directories in tmp:"
        find "$TMPPATH" -type d | head -20
        cleanup
        exit 1
    fi
fi

sync

echo "Verifying installation..."
if [ -d "$PLUGINPATH" ] && [ -n "$(ls -A "$PLUGINPATH" 2>/dev/null)" ]; then
    echo "Plugin directory found and not empty: $PLUGINPATH"
    echo "Contents:"
    ls -la "$PLUGINPATH/" | head -10
else
    echo "Plugin installation failed or directory is empty!"
    cleanup
    exit 1
fi

cleanup
sync

# ============================================================
# GET SYSTEM INFO
# ============================================================
FILE="/etc/image-version"
box_type=$(sed -n '1p' /etc/hostname 2>/dev/null || echo "Unknown")

if [ -r /etc/os-release ]; then
    distro_value=$(grep '^NAME=' /etc/os-release 2>/dev/null | cut -d'"' -f2)
    distro_version=$(grep '^VERSION_ID=' /etc/os-release 2>/dev/null | cut -d'"' -f2)
elif [ -r /etc/issue ]; then
    distro_value=$(head -n 1 /etc/issue 2>/dev/null | awk '{print $1}')
    distro_version=$(head -n 1 /etc/issue 2>/dev/null | awk '{print $2}')
elif [ -r /etc/vtiversion.info ]; then
    distro_value=$(head -n 1 /etc/vtiversion.info 2>/dev/null)
elif [ -r /etc/issue.net ]; then
    distro_value=$(head -n 1 /etc/issue.net 2>/dev/null | awk '{print $1}')
    distro_version=$(head -n 1 /etc/issue.net 2>/dev/null | awk '{print $2}')
fi

[ -z "$distro_value" ] && distro_value="Unknown"
[ -z "$distro_version" ] && distro_version="Unknown"
python_vers=$(python --version 2>&1)

cat <<EOF

#########################################################
#               INSTALLED SUCCESSFULLY                  #
#          LottoStatistiche - Lotto Statistics          #
#########################################################
#           your Device will RESTART Now                #
#########################################################
^^^^^^^^^^Debug information:
BOX MODEL: $box_type
OS SYSTEM: $OSTYPE
PYTHON: $python_vers
IMAGE NAME: ${distro_value:-Unknown}
IMAGE VERSION: ${distro_version:-Unknown}
PLUGIN VERSION: $version
#########################################################
#         NO DEPENDENCIES REQUIRED                       #
#         Plugin uses only standard Enigma2 libs        #
#########################################################
EOF

exit 0