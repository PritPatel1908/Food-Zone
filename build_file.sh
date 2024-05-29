#!/bin/bash

# Collect static files
python3 -m manage.py collectstatic

# Create a tarball of the staticfiles_build directory
tar -czf staticfiles_build.tar.gz staticfiles_build

# Upload the tarball to Vercel
vercel deploy staticfiles_build.tar.gz