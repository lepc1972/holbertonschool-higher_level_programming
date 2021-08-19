#!/bin/bash
# script show status code
curl -s -X HEAD -w "%{http_code}" "$1"
