#!/bin/bash

# Add all changes to git
git add .

# Check if commit message was provided as argument
if [ "$1" ]; then
    git commit -m "$1"
else
    echo "Error: Please provide a commit message"
    echo "Usage: ./scripts/quick_commit.sh \"your commit message\""
    exit 1
fi

# Push to main branch
git push origin main

# chmod +x quick_commit.sh   
# ./scripts/quick_commit.sh "test"