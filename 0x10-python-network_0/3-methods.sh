#!/bin/bash
#display HTTP methods server will take
curl -sI -X OPTIONS "$1" | sed -n -e '/Allow/ s/.*\: *//p'
