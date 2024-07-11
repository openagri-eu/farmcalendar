#!/bin/bash

# Exit script on error
set -e

# Run initial_setup file
echo "Running initial setup"
python3 manage.py initial_setup

# Start the Django app with waitress
echo "Starting Django server with Waitress..."
exec python3 run_waitress.py
