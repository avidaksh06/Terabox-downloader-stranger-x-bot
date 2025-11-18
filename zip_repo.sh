#!/usr/bin/env bash
set -e
ROOT="$(pwd)"
NAME="terabox-pyro-userbot"
zip -r "${NAME}.zip" README.md main.py extractor.py requirements.txt render.yaml .env.example .gitignore LICENSE
echo "Created ${NAME}.zip"
