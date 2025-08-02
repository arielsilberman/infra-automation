#!/bin/bash

SERVICE=$1
LOG_FILE="logs/provisioning.log"

log() {
  echo "$(date '+%H:%M:%S %Y-%m-%d') - $1" >> "$LOG_FILE"
}

if [[ "$SERVICE" == "" ]]; then
  echo "Select a valid service option please..."
  log "No service input by user for installation"
  exit 1
fi

echo "Starting installation of $SERVICE... Please wait a few seconds"
log "Starting installation of $SERVICE... Please wait a few seconds"
sleep 3
echo "$SERVICE installed successfully."
log "$SERVICE installed successfully."

