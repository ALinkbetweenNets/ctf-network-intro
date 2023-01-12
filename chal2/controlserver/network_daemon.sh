#!/bin/bash
while true 
do
    echo -e "GET / HTTP 1.1\n\n" | nc 172.28.3.2 80 -vvv
    sleep 1
done