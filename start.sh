#!/bin/sh

pkill boomajoom_temp_pid
../bin/gunicorn --config gunicorn.py boomajoom_temp.wsgi:application --daemon --pid boomajoom_temp_pid