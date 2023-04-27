#!/bin/bash
#write bash script
url=$1
size=$(curl -sI $url | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

echo "Size of the response body: $size bytes"
