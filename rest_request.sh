#!/bin/bash

curl -XPOST -H 'Content-Type:application/json' -H 'Accept: application/json' -d "@rest_request_sample.json" http://localhost:5000/api/summarizer

echo
