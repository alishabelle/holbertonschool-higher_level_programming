#!/bin/bash
#takes in url sends request, displays size of body response
curl -s "$1" | wc -c 
