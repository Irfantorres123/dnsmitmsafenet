#!/bin/bash
mitmdump -p 443 -s intercept.py --mode reverse:https://www.google.com/ &
P1=$!
mitmdump -p 80 -s intercept.py --mode reverse:https://localhost:443/  --set keep_host_header &
P2=$!
wait $P1 $P2