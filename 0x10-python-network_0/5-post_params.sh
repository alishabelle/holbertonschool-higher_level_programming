#!/bin/bash
#sends a POST request to passed URL
curl -s -X POST -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" "$1"
