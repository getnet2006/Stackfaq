#!/bin/sh
gunicorn --chdir app run:app -w 2 --threads 2 -b 0.0.0.0:8088