#!/bin/bash
# script post request with json
curl -s -X PUT -d user_id=98 -d '{"Allow: OPTIONS, PUT, GET, POST"}' 0.0.0.0:5000/catch_me -L -H "Origin: HolbertonSchool"
