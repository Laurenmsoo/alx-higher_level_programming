#!/bin/bash
# Gets the size of the response
curl -s "$1" | wc -c
