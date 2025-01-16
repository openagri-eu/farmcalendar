#!/bin/bash

# Exit script on error
set -e

# re-generating schema.yml
echo "re-generating and validating schema.yml"
python3 manage.py spectacular --validate --color --file schema.yml

# registrating endpoints
echo "running service registration"
python3 manage.py service_registration

# Run initial_setup file
echo "Running initial setup"
python3 manage.py initial_setup

# Start the Django app with waitress
echo "Starting Django server with Waitress..."
exec python3 run_waitress.py
