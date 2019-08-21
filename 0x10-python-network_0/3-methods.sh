#!/bin/bash
#display HTTP methods server will take
curl -s -X OPTIONS "$1" | sed -n -e '/Allow/ s/.*\: *//p
