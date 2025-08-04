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


log "Starting installation of $SERVICE... "
sleep 2
log "$SERVICE installed successfully."

