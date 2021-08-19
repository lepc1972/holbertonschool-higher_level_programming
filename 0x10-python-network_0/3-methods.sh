#!/bin/bash
# script that displays HTTP methods
curl -sI "$1" | sed -n 's/Allow: //p'
