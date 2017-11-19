#!/bin/sh
dirpo4md=$(dirname "$0")
/usr/bin/python3 ${dirpo4md}/tools/createpot.py
/usr/bin/python3 ${dirpo4md}/tools/updatepo.py
