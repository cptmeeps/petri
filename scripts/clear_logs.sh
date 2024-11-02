#!/bin/bash

# Path to logs directory from project root
LOGS_DIR="logs"

# Check if logs directory exists
if [ ! -d "$LOGS_DIR" ]; then
    echo "Logs directory not found!"
    exit 1
fi

# Remove all .txt files in the logs directory
rm -f "$LOGS_DIR"/*.txt

echo "All log files have been cleared!" 

# chmod +x scripts/clear_logs.sh
# ./scripts/clear_logs.sh