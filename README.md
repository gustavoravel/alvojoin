# Join Tecnologia - Target Django Project

This is a simple Django project that lists targets and locations. You can easily run it using the provided scripts.

## Prerequisites

Make sure you have Python and Django installed on your system.

## Virtual Environment Configuration

Run one of the following files to configure a virtual environment and install project requirements:

start_project_linux.sh (Linux)

start_project_windows.ps1 (Windows)

## Admin

user:admin

password:admin

## Tests

Run these commands to execute tests:

coverage run --omit='\*/venv/\*' manage.py test

coverage html

The server will be available at http://localhost:8000/.