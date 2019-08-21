#!/bin/bash
#display status code
curl -s -X HEAD -w "%{http_code}" "$1"
