#!/bin/bash 

ip route add ${PEER_SUBNET} via ${PEER_GATEWAY}

socat tcp-l:1337,reuseaddr,fork EXEC:'python vuln.py',pty,stderr