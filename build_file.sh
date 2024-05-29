#!/bin/bash

# Collect static files
python3 -m manage.py collectstatic

# Create a tarball of the media directory
tar -czf media.tar.gz media

# Upload the tarball to Vercel
vercel deploy media.tar.gz