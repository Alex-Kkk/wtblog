#!/bin/bash

FILENAME=/root/regular_report.txt
CURRENT_DATE=$(date '+%Y-%m-%d %H:%M:%S')

set -e

cd wtblog

echo "$CURRENT_DATE update cert init" >> "$FILENAME"

docker compose run --rm certbot sh -c "certbot renew" >> "$FILENAME" 2>&1
docker compose restart >> "$FILENAME" 2>&1

echo "$CURRENT_DATE update complete" >> "$FILENAME"
