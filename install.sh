#!/bin/bash

# Check if jq is installed
if ! [ -x "$(command -v jq)" ]; then
  echo 'Error: jq is not installed.' >&2
  exit 1
fi

# Download latest release
RELEASE=$(curl -s 'https://api.github.com/repos/survfate/ayaled-decky/releases/latest')
RELEASE_VERSION=$(echo "$RELEASE" | jq -r '.tag_name')
RELEASE_URL=$(echo "$RELEASE" | jq -r '.assets[0].browser_download_url')
curl -L -o /tmp/ayaled-decky.tar.gz "$RELEASE_URL"

echo "Installing ayaled-decky $RELEASE_VERSION"

# Remove old version
chmod -R 777 ${HOME}/homebrew/plugins
rm -rf ${HOME}/homebrew/plugins/ayaled-decky

# Extract & Cleanup
tar -xzf /tmp/ayaled-decky.tar.gz -C ${HOME}/homebrew/plugins && rm -f /tmp/ayaled-decky.tar.gz

echo "ayaled-decky $RELEASE_VERSION installed"

# Restart plugin_loader
sudo systemctl restart plugin_loader.service